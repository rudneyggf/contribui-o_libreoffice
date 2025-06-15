# Macro de Conversão de Riot Points para Reais no LibreOffice Calc

## Visão Geral
Esta é uma macro Python para o LibreOffice Calc que converte Pontos de Riot (RP) em Reais (BRL), com base em uma taxa de conversão média.

## Como Instalar

### No Windows:
1. Baixe o script de macro: `macroRP.py`.
2. Copie o script `macroRP.py` para o diretório de macros Python do LibreOffice:
- `C:\Usuários\<SeuNomeDeUsuário>\AppData\Roaming\LibreOffice\4\usuário\Scripts\python\`
3. Reinicie o LibreOffice Calc.
4. Abra o LibreOffice Calc e selecione as células com os valores de Pontos de Riot (RP).
5. Acesse **Ferramentas > Macros > Organizar Macros > Python...**
6. Selecione **Macros de Usuário > macroRP > converter_para_reais** e clique em **Executar**.

### No Linux:
1. Baixe o script de macro: `macroRP.py`.
2. Copie o script para o diretório de macros do Python do seu LibreOffice:
- `~/.config/libreoffice/4/user/Scripts/python/`
- Você pode usar o comando de terminal:
```bash
mkdir -p ~/.config/libreoffice/4/user/Scripts/python/
cp macroRP.py ~/.config/libreoffice/4/user/Scripts/python/
```
3. Reinicie o LibreOffice Calc.
4. Abra o LibreOffice Calc e selecione as células com os valores de Pontos de Riot (RP).
5. Acesse **Ferramentas > Macros > Organizar Macros > Python...**
6. Selecione **Macros de Usuário > macroRP > converter_para_reais** e clique em **Executar**.

## Licença
Este script é gratuito para uso e distribuição e está regido pela GNU Lesser General Public License version 3 (LGPL v3)

Caso tenha alguma dúvida ou sugestão, entre em contato com o autor: Rudney.
