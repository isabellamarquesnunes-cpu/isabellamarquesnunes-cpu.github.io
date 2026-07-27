# LandingPage — Isabella Marques

Landing page da **Isabella Marques Nunes** — "Especialista em Cachos". **Marca pessoal da sócia, não é produto Atlas.** Projeto independente, com repositório git próprio nesta pasta.

## Estrutura real

```
LandingPage/
├── index.html                      # Página única: landing + catálogo de serviços + galeria (CSS/JS inline)
├── catalogo.html                   # Só redirect para index.html#servicos (links antigos)
├── Catalogo-Isabella-Marques.pdf   # Catálogo em PDF pra mandar no WhatsApp
├── hero-isabella.webp              # Hero otimizado (289 KB) — o que o site usa
├── hero-fallback.png               # Fallback do <picture> p/ navegadores sem WebP
├── hero-isabella.png               # Original 2,7 MB — FORA do git (só fonte local)
├── og-image.jpg                    # Prévia de compartilhamento (1200x630)
├── favicon-32.png / apple-touch-icon.png
└── fotos/                          # Resultados otimizados (JPEG ~170 KB, máx. 1000px)
```

Serviços/preços vivem na lista `SERVICOS` no `<script>` de `index.html` — editar SÓ ali. Galeria idem, lista `GALERIA`. Dois itens `PENDENTE` (Combo Umectação sem preço; descrição do Peeling cortada). O PDF é gerado por script (pedir ao Claude pra regenerar quando os preços mudarem).

## Publicação

GitHub Pages na conta da Isabella (`isabellamarquesnunes-cpu`), repositório `isabellamarquesnunes-cpu.github.io` → https://isabellamarquesnunes-cpu.github.io/ . As metas OG e o JSON-LD já apontam pra essa URL — se migrar de domínio, trocar nos dois lugares no `<head>`.

## Regra crítica — paleta é DELA, não Atlas

Rosa `#b15f7d` · vinho `#6b2947` · oliva `#53614b` · dourado `#ba8a50`. Fontes: Playfair Display + Nunito. **Não aplicar paleta Atlas.** Quem "padronizar" pra marfim/marinho/dourado-queimado quebra a marca — reprovar.

## Regras que continuam valendo

- HTML/CSS/JS nativos. Sem React/Vue/Tailwind/jQuery.
- Correção de estilo é global: achou problema numa seção, varra todas.
- Testar no navegador de verdade (desktop + mobile) antes de dar por pronto.

## Como rodar localmente

```bash
python -m http.server 8712
# abrir http://localhost:8712/
```

## Histórico

- Havia uma "Curadoria de produtos" (index.html antigo) — a Isabella decidiu excluir; ficou só a landing de serviços.
- A pasta original era `C:\Projetos\SI\Landing Page - Isabella` (pode ser apagada; tudo que vale está aqui).

## Stakeholders

Isabella Marques Nunes — decisões de conteúdo/paleta são dela.
