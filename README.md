# GuaipeCare

Coleira inteligente de baixo custo para cães e gatos comunitários. Uma tag NFC na coleira abre uma página web com o perfil do animal (saúde, vacinas, contato dos cuidadores) e registra o último local de avistamento, mediante autorização de quem escaneia.

Projeto da disciplina de **Metodologia Científica para Computação** (UFPEL).
Professoras: Ana Marilza Pernas e Tatiana Aires.

## Problema

Comunidades, condomínios e ONGs cuidam de animais de rua, mas as informações sobre cada animal ficam dispersas, o que dificulta acompanhar saúde, vacinas e localização.

## Como funciona

1. O cuidador cadastra o animal no site e recebe uma URL única (`/a/<id>`).
2. Essa URL é gravada em uma tag NFC presa à coleira.
3. Ao aproximar o celular da coleira, a página do animal abre no navegador.
4. Se a pessoa permitir, o navegador envia a localização e o sistema salva o **último avistamento** (coordenadas e horário).

A localização não é rastreamento em tempo real: só é atualizada quando alguém escaneia a coleira.

## Funcionalidades (MVP)

- [ ] Página pública do animal (foto, nome, espécie, vacinas, contato)
- [ ] Registro de avistamento por geolocalização do navegador
- [ ] Login de cuidadores
- [ ] Cadastro e edição de animais e vacinas
- [ ] Mapa com histórico de avistamentos (somente logado)
- [ ] Regras de visibilidade (dados públicos x restritos)

## Tecnologias

| Camada | Ferramenta |
|---|---|
| Backend | Python + Flask |
| Templates | Jinja2 + HTML |
| Banco de dados | SQLite + SQLAlchemy |
| Autenticação | Flask-Login |
| Mapa | Leaflet + OpenStreetMap |
| Hardware | Tags NFC |

## Estrutura do projeto

```
guaipecare/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes_public.py
│   ├── routes_admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── animal.html
│   │   └── admin/
│   └── static/
│       ├── css/style.css
│       ├── js/geolocalizacao.js
│       └── uploads/
├── docs/
│   └── canvas_guaipecare.pdf
├── config.py
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

## Como executar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate           # Linux/macOS: source .venv/bin/activate

# instalar as dependências
pip install -r requirements.txt

# iniciar o servidor de desenvolvimento
python run.py
```

Acesse `http://localhost:5000`.

> A geolocalização do navegador só funciona em `localhost` ou em **HTTPS**. Para testar com o celular e a tag NFC, use um túnel HTTPS (cloudflared, ngrok) ou o encaminhamento de porta do GitHub Codespaces.

## Privacidade

- A localização só é coletada com permissão explícita do navegador.
- Nenhuma informação que identifique quem escaneou é armazenada.
- O histórico detalhado de localização é visível apenas para cuidadores autenticados.
- IDs públicos dos animais são aleatórios (UUID), nunca sequenciais.

## Riscos conhecidos

- Baixa adesão dos cuidadores na atualização dos perfis
- Coleira danificada ou ingerida (usar modelo com fecho de segurança)
- Compatibilidade NFC em aparelhos mais antigos (previsto QR code como alternativa)
- Exposição indevida de localização do animal

## Equipe

- Lucas Dias
- Lúcio Vagner
- Luísa Böhm

## Licença

A definir.
