/* Gráficos do artigo. Todos os dados e bibliotecas estão no próprio HTML. */
const D = window.DADOS;
const EMP = ['BAC','JNJ','KO','NFLX','NVDA'];
const CORES = {BAC:'#32648d',JNJ:'#b27615',KO:'#16877b',NFLX:'#8664a5',NVDA:'#bd5b3a',negativo:'#bd5b3a',neutro:'#83929f',positivo:'#16877b',empate:'#8664a5'};
const CEN = ['Principal','Mínimo 3','Sem retrospectivas','Sem retrospectivas + mínimo 3'];
const esc = s => String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const fmt=(n,k=3)=>Number(n).toLocaleString('pt-BR',{minimumFractionDigits:k,maximumFractionDigits:k});
const dia=s=>String(s).slice(0,10);
const registro = Object.fromEntries(D.noticias.map(n=>[n.source_id,n]));
const indiceDia={}, indicePregao={};
D.noticias.forEach(n=>{const kd=n.stock+'|'+dia(n.news_date), kp=n.stock+'|'+dia(n.trade_date);(indiceDia[kd]??=[]).push(n.source_id);(indicePregao[kp]??=[]).push(n.source_id);});
let listaAtual=[], pagina=0;
function noticiasDoPonto(modo,key) { return (modo==='dia'?indiceDia:indicePregao)[key]??[]; }
function previa(ids,titulo) {
  const el=document.getElementById('previa'); if(!el)return;
  el.innerHTML='<strong>'+esc(titulo)+'</strong><br>'+ids.slice(0,3).map(id=>{
    const n=registro[id];return esc(n.headline)+' <span class="muted">('+esc(n.assunto)+')</span>';
  }).join('<br>')+(ids.length>3?'<br><span class="muted">Mais '+(ids.length-3)+' manchetes. Clique no ponto para consultar a lista.</span>':'');
}
function abrir(ids,titulo) {
  listaAtual=ids.map(id=>registro[id]);pagina=0;
  document.getElementById('lista-titulo').textContent=titulo+' · '+ids.length+' associações';
  document.getElementById('lista-busca').value='';document.getElementById('consulta').hidden=false;renderLista();
  document.getElementById('lista-titulo').focus();
}
function renderLista(){
  const q=document.getElementById('lista-busca').value.toLocaleLowerCase('pt-BR');
  const dados=listaAtual.filter(n=>(n.headline+' '+n.assunto+' '+n.stock+' '+n.publisher).toLocaleLowerCase('pt-BR').includes(q));
  const max=Math.max(1,Math.ceil(dados.length/20));pagina=Math.min(pagina,max-1);
  const lista=document.getElementById('lista');lista.replaceChildren();
  dados.slice(pagina*20,pagina*20+20).forEach(n=>{
    const art=document.createElement('article'); const h=document.createElement('h4'); h.textContent=n.headline;art.append(h);
    const assunto=document.createElement('p');assunto.textContent='Assunto sugerido pela manchete: '+n.assunto;art.append(assunto);
    const meta=document.createElement('p');meta.className='muted';meta.textContent=n.stock+' · notícia '+dia(n.news_date)+' · pregão '+dia(n.trade_date)+' · '+n.classe_finbert+' · escore '+fmt(n.escore_sentimento)+' · '+(n.publisher||'Fonte não informada');art.append(meta);
    try {const u=new URL(n.url);if(['https:','http:'].includes(u.protocol)){const a=document.createElement('a');a.href=u.href;a.target='_blank';a.rel='noopener noreferrer';a.textContent='Abrir matéria original';art.append(a);}}catch{}
    lista.append(art);
  });
  document.getElementById('paginacao').textContent=dados.length+' resultados · página '+(pagina+1)+' de '+max;
  document.getElementById('anterior').disabled=pagina===0;document.getElementById('proxima').disabled=pagina>=max-1;
}
document.getElementById('lista-busca')?.addEventListener('input',()=>{pagina=0;renderLista();});
document.getElementById('anterior')?.addEventListener('click',()=>{pagina--;renderLista();});
document.getElementById('proxima')?.addEventListener('click',()=>{pagina++;renderLista();});
document.getElementById('fechar')?.addEventListener('click',()=>document.getElementById('consulta').hidden=true);
document.addEventListener('keydown',e=>{if(e.key==='Escape')document.getElementById('consulta').hidden=true;});
document.getElementById('todas-noticias')?.addEventListener('click',()=>abrir(D.noticias.map(n=>n.source_id),'Todas as notícias'));
function hover(modo,key,rotulo){const ids=noticiasDoPonto(modo,key);return esc(rotulo).replace(/&lt;br&gt;/g,'<br>')+'<br>'+ids.length+' notícia(s)<br>'+ids.slice(0,3).map(id=>{const n=registro[id];return esc(n.headline).replace(/(.{58})\s/g,'$1<br>')+'<br><i>'+esc(n.assunto)+'</i>';}).join('<br><br>')+(ids.length>3?'<br>Mais '+(ids.length-3)+' manchetes.':'')+'<br><i>Clique para consultar todas.</i>';}
function ligar(el,modo){
  el.on('plotly_hover',ev=>{const p=ev.points[0];if(p.customdata?.[0])previa(noticiasDoPonto(modo,p.customdata[0]),p.customdata[0]);});
  el.on('plotly_click',ev=>{const p=ev.points[0];if(p.customdata?.[0])abrir(noticiasDoPonto(modo,p.customdata[0]),p.customdata[0]);});
}
const base={font:{family:'Arial, sans-serif',size:13,color:'#203448'},paper_bgcolor:'#fff',plot_bgcolor:'#fff',margin:{l:70,r:25,t:30,b:65},hoverlabel:{align:'left',font:{size:13}},legend:{orientation:'h',y:-.23},colorway:EMP.map(e=>CORES[e])};
const config={responsive:true,displaylogo:false,scrollZoom:false,toImageButtonOptions:{format:'png',scale:2}};
async function plot(id,traces,layout={},modo=null){const el=document.getElementById(id);if(!el)return;await Plotly.newPlot(el,traces,{...base,...layout},config);if(modo)ligar(el,modo);}
function selecionadas(rows){const e=document.getElementById('empresa')?.value??'Todas';const ano=document.getElementById('ano')?.value??'Todos';return rows.filter(p=>(e==='Todas'||p.stock===e)&&(ano==='Todos'||dia(p.trade_date??p.news_date).startsWith(ano)));}
function pontos(rows,x,y,modo){const nomes={n_noticias:'Notícias',escore_sentimento:'Escore',retorno_pct:'Retorno (%)',retorno_absoluto_pct:'Retorno absoluto (%)',polarizacao_liquida:'Polarização líquida',intensidade_media:'Intensidade média'};return EMP.map(e=>{const g=rows.filter(p=>p.stock===e);return {type:'scatter',mode:'markers',name:e,x:g.map(p=>p[x]),y:g.map(p=>p[y]),customdata:g.map(p=>[p.key]),text:g.map(p=>hover(modo,p.key,e+' · '+dia(p.trade_date??p.news_date)+'<br>'+(x==='news_date'?'':nomes[x]+': '+fmt(p[x])+' · ')+nomes[y]+': '+fmt(p[y]))),hovertemplate:'%{text}<extra></extra>',marker:{size:7,opacity:.6,color:CORES[e]},showlegend:true};});}
async function desenhar(){
 const all=D.principal, pr=selecionadas(all), diario=selecionadas(D.diario);
 const retornoMin=Math.min(...all.map(p=>p.retorno_pct))-1, retornoMax=Math.max(...all.map(p=>p.retorno_pct))+1;
 const absolutoMax=Math.max(...all.map(p=>p.retorno_absoluto_pct))*1.05;
 const ano=document.getElementById('ano')?.value??'Todos';const e=document.getElementById('empresa')?.value??'Todas';
 const ns=D.noticias.filter(n=>(e==='Todas'||n.stock===e)&&(ano==='Todos'||dia(n.news_date).startsWith(ano)));
 const empresas=e==='Todas'?EMP:[e];
 const meses=[...new Set(D.q1_mensal.map(r=>dia(r.mes).slice(0,7)))].filter(m=>ano==='Todos'||m.startsWith(ano));
 const mat=empresas.map(e=>meses.map(m=>D.q1_mensal.find(r=>r.stock===e&&dia(r.mes).startsWith(m))?.n??0));
 const el1=document.getElementById('q1');
 if(el1){await plot('q1',[{type:'heatmap',x:meses,y:empresas,z:mat,colorscale:'Blues',zmin:0,zmax:Math.max(...D.q1_mensal.map(r=>r.n)),hovertemplate:'%{y} · %{x}<br>%{z} notícias<extra></extra>',colorbar:{title:'Notícias'}}],{height:330,xaxis:{title:{text:'Mês da notícia'},tickangle:-50},yaxis:{title:{text:'Empresa'},autorange:'reversed'}});el1.removeAllListeners('plotly_click');el1.removeAllListeners('plotly_hover');const ids=p=>ns.filter(n=>n.stock===p.y&&dia(n.news_date).startsWith(p.x)).map(n=>n.source_id);el1.on('plotly_click',ev=>abrir(ids(ev.points[0]),ev.points[0].y+' · '+ev.points[0].x));el1.on('plotly_hover',ev=>previa(ids(ev.points[0]),ev.points[0].y+' · '+ev.points[0].x));}
 const traces2=['negativo','neutro','positivo','empate'].map(c=>({type:'bar',name:c,orientation:'h',y:empresas,x:empresas.map(e=>{const rows=ns.filter(n=>n.stock===e);return rows.length?100*rows.filter(n=>n.classe_finbert===c).length/rows.length:0;}),marker:{color:CORES[c]},customdata:empresas.map(e=>[e,c,ns.filter(n=>n.stock===e&&n.classe_finbert===c).length,ns.filter(n=>n.stock===e).length]),hovertemplate:'%{customdata[0]} · %{customdata[1]}<br>%{x:.1f}% · n=%{customdata[2]} de %{customdata[3]}<extra></extra>'}));
 await plot('q2',traces2,{height:350,barmode:'stack',xaxis:{title:{text:'Proporção de manchetes (%)'},range:[0,100]},yaxis:{autorange:'reversed'},legend:{orientation:'h',y:-.35}});
 const el2=document.getElementById('q2');if(el2){const ids=p=>ns.filter(n=>n.stock===p.customdata[0]&&n.classe_finbert===p.customdata[1]).map(n=>n.source_id);el2.on('plotly_hover',ev=>previa(ids(ev.points[0]),ev.points[0].customdata.slice(0,2).join(' · ')));el2.on('plotly_click',ev=>abrir(ids(ev.points[0]),ev.points[0].customdata.slice(0,2).join(' · ')));}
 await plot('q3',pontos(diario,'news_date','escore_sentimento','dia'),{height:430,xaxis:{title:{text:'Data civil da notícia'},range:['2017-01-01','2020-01-01'],rangeslider:{visible:true,thickness:.13}},yaxis:{title:{text:'Escore médio'},range:[-1,1]},legend:{orientation:'h',y:-.35}},'dia');
 const q4=[];
 empresas.forEach((e,i)=>{const g=pr.filter(p=>p.stock===e);['negativo','neutro','positivo'].forEach(c=>{const r=g.filter(p=>p.classe_sentimento===c);q4.push({type:'box',x:r.map(()=>c),y:r.map(p=>p.retorno_pct),name:c,marker:{color:CORES[c]},line:{color:CORES[c]},boxpoints:false,showlegend:false,xaxis:i?'x'+(i+1):'x',yaxis:i?'y'+(i+1):'y'});q4.push({type:'scatter',mode:'markers',name:e,x:r.map(()=>c),y:r.map(p=>p.retorno_pct),customdata:r.map(p=>[p.key]),text:r.map(p=>hover('pregao',p.key,e+' · '+dia(p.trade_date)+' · '+fmt(p.retorno_pct)+'%')),hovertemplate:'%{text}<extra></extra>',marker:{size:5,color:CORES[c],opacity:.28},showlegend:false,xaxis:i?'x'+(i+1):'x',yaxis:i?'y'+(i+1):'y'});});});
 const cols=empresas.length===1||window.innerWidth<700?1:3, rows=Math.ceil(empresas.length/cols);const l4={height:rows*320,margin:{l:65,r:20,t:35,b:55},annotations:[]};
 empresas.forEach((e,i)=>{const col=i%cols,row=Math.floor(i/cols);const x='xaxis'+(i?i+1:''),y='yaxis'+(i?i+1:'');l4[x]={domain:[col/cols+.025,(col+1)/cols-.035],anchor:i?'y'+(i+1):'y',categoryorder:'array',categoryarray:['negativo','neutro','positivo']};l4[y]={domain:[1-(row+1)/rows+.09/rows*2,1-row/rows-.09/rows*2],anchor:i?'x'+(i+1):'x',range:[retornoMin,retornoMax],title:{text:col===0?'Retorno (%)':''},zerolinecolor:'#8795a3'};l4.annotations.push({xref:'paper',yref:'paper',x:(col+.5)/cols,y:1-row/rows-.03/rows*2,text:e+' · n='+pr.filter(p=>p.stock===e).length,showarrow:false});});
 await plot('q4',q4,l4,'pregao');
 const met=document.getElementById('medida')?.value??'polarizacao_liquida';
 const tituloMed=met==='intensidade_media'?'Intensidade média = média(|sᵢ|)':'Polarização líquida = |média(sᵢ)|';
 const tr5=pontos(pr,'n_noticias','retorno_absoluto_pct','pregao').concat(pontos(pr,met,'retorno_absoluto_pct','pregao').map(t=>({...t,xaxis:'x2',yaxis:'y2',showlegend:false})));
 const mobile=window.innerWidth<700;
 await plot('q5',tr5,{height:mobile?700:430,xaxis:{domain:mobile?[0,1]:[0,.44],title:{text:'Número de notícias'},range:[0,Math.max(...all.map(p=>p.n_noticias))+1]},yaxis:{domain:mobile?[.58,1]:[0,1],title:{text:'Retorno absoluto (%)'},range:[0,absolutoMax]},xaxis2:{domain:mobile?[0,1]:[.56,1],anchor:'y2',title:{text:tituloMed},range:[0,1]},yaxis2:{domain:mobile?[0,.42]:[0,1],anchor:'x2',range:[0,absolutoMax],showticklabels:mobile}},'pregao');
 const periods=['2017','2018','2019','2017–2019'];
 const corr=(e,p)=>D.q6_correlacoes.find(r=>r.stock===e&&r.periodo===p);
 const cmat=empresas.map(e=>periods.map(p=>corr(e,p)?.rho));
 const ctext=empresas.map(e=>periods.map(p=>{const r=corr(e,p);return r?fmt(r.rho)+'<br>n='+r.n:'';}));
 await plot('q6',[{type:'heatmap',x:periods,y:empresas,z:cmat,text:ctext,texttemplate:'%{text}',zmin:-1,zmax:1,colorscale:[[0,'#bd5b3a'],[.5,'#f7f8fa'],[1,'#32648d']],hovertemplate:'%{y} · %{x}<br>ρ=%{z:.4f}<br>%{text}<extra></extra>',colorbar:{title:'ρ'}}],{height:370,yaxis:{autorange:'reversed'},xaxis:{type:'category',categoryorder:'array',categoryarray:periods,title:{text:'Ano do pregão de resposta'}}});
 const el6=document.getElementById('q6');if(el6)el6.on('plotly_click',async ev=>{const p=ev.points[0];const rows=all.filter(r=>r.stock===p.y&&(p.x==='2017–2019'||String(r.ano)===p.x));await plot('q6-detalhe',pontos(rows,'escore_sentimento','retorno_pct','pregao'),{height:360,xaxis:{range:[-1,1],title:{text:'Escore agregado'}},yaxis:{range:[-20,20],title:{text:'Retorno (%)'}},title:{text:p.y+' · '+p.x+' · n='+rows.length,font:{size:15}}},'pregao');});
 const met7=document.getElementById('metrica-robustez')?.value??'Escore × retorno';
 const tr7=CEN.map((c,i)=>{const g=D.q7_sensibilidade.filter(r=>r.cenario===c&&r.metrica===met7&&(e==='Todas'||r.stock===e));return {type:'scatter',mode:'markers',name:c,x:g.map(r=>r.rho),y:g.map(r=>EMP.indexOf(r.stock)+(i-1.5)*.13),text:g.map(r=>r.stock+' · '+c+'<br>ρ='+fmt(r.rho,4)+' · n='+r.n),hovertemplate:'%{text}<extra></extra>',marker:{size:11,symbol:['circle','square','triangle-up','cross'][i],color:['#32648d','#bd5b3a','#16877b','#8664a5'][i]}};});
 await plot('q7',tr7,{height:440,xaxis:{range:[-1,1],title:{text:met7+' · Spearman (ρ)'},zerolinecolor:'#83929f'},yaxis:{tickvals:[0,1,2,3,4],ticktext:EMP,autorange:'reversed'},legend:{orientation:'h',y:-.23}});
 const status=document.getElementById('filtro-status');if(status)status.textContent=ns.length+' associações por data da notícia · '+pr.length+' pares elegíveis por data do pregão. Q6 e Q7 mantêm os períodos e cenários indicados.';
 window.graficosProntos=true;
}
['empresa','ano','medida','metrica-robustez'].forEach(id=>document.getElementById(id)?.addEventListener('change',()=>desenhar().catch(console.error)));
desenhar().catch(e=>{console.error(e);document.getElementById('filtro-status').textContent='Não foi possível desenhar: '+e.message;});
