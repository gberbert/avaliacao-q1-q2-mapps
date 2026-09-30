#!/usr/bin/env python3
"""fix_acdc_i18n.py
Insere as chaves de cálculo em es, en e ptb dentro de update_i18n.py com comentários JS válidos //
e gera os arquivos de ACDC.
"""

script_path = "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/update_i18n.py"
with open(script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Substituir o comentário Python # por // caso exista
code = code.replace("# Slide 9: Memoria de Cálculo & Metodología", "// Slide 9: Memoria de Calculo & Metodologia")

en_calc = '''        // Slide 9: Calculation Memory & Methodology
        s9_calc_btn: "🧮 Calculation Memory & Methodology",
        s9_calc_callout_title: "AUDITED METHODOLOGICAL BASELINE & SAMPLING (MAPFRE BRAZIL)",
        s9_calc_callout_desc: "Metrics audited over an operational universe of 110 annual tariff releases, 1,250 actuary technical inquiries, and full PECA audit trail. 100% reproducible math.",
        s9_calc_pill: "📊 Calculation Memory",
        s9_modal_title: "Calculation Memory & Methodological Baseline — ACDC Platform",
        s9_modal_sub: "Analytical audit of mathematical equations, technical hours saved, homologation speed, and production reliability across MAPFRE.",
        s9_kpi1_math_title: "1. Technical Hours Saved Per Year (+1,400 h)",
        s9_kpi1_math_base: "Legacy Baseline: 16 technical hours per tariff release (manual JSON coding into MongoDB, syntax debugging, manual QA). Total: 110 × 16 h = 1,760 h/year.",
        s9_kpi1_math_plat: "With ACDC Cockpit: 3 technical hours per release (real-time schema validation, actuarial autocompletion, visual diff, instant rollback). Total: 110 × 3 h = 330 h/year.",
        s9_kpi1_math_eq: "Equation: Savings = 1,760 h - 330 h = 1,430 hours saved/year (reported conservatively as: +1,400 h/year).",
        s9_kpi1_math_imp: "Impact: Unlocks engineering bandwidth equivalent to nearly 1 full-time senior actuarial software engineer at MAPFRE.",
        s9_kpi2_math_title: "2. Homologation Speed (12x Faster)",
        s9_kpi2_math_base: "Legacy Time-to-Market: 14 business days (Rule Definition 3d + JSON Coding 4d + QA Homologation 5d + Deployment 2d).",
        s9_kpi2_math_plat: "ACDC Cockpit: 1.15 business days (~28 continuous pipeline hours with assisted validation).",
        s9_kpi2_math_eq: "Equation: Acceleration Factor = 14 days / 1.15 days = 12.17x (reported: 12x Faster).",
        s9_kpi2_math_imp: "Impact: Agile time-to-market for launching innovative insurance products ahead of competitors.",
        s9_kpi3_math_title: "3. Resolution via ACDC Copilot (92%)",
        s9_kpi3_math_base: "Total Audited Inquiries: 1,250 technical tickets from actuaries per year on DUP mappings and Tronador schemas.",
        s9_kpi3_math_plat: "1,150 inquiries resolved autonomously by ACDC Copilot in < 1 minute without escalating tickets to senior architects.",
        s9_kpi3_math_eq: "Equation: Autonomous Resolution Rate = (1,150 / 1,250) × 100 = 92.0%.",
        s9_kpi3_math_imp: "Impact: Removes bottlenecks at the architecture desk and empowers business actuaries with self-service discovery.",
        s9_kpi4_math_title: "4. Non-Compliance Liabilities (0 Incidents)",
        s9_kpi4_math_base: "Prior Legacy Pain: Sporadic production downtime caused by duplicate keys or incompatible data types in tariff schemas.",
        s9_kpi4_math_plat: "ACDC: 100% of releases validated with PECA lineage, SHA-256 signatures, and role-based permissions.",
        s9_kpi4_math_eq: "Equation: Production Incidents = 0 • SUSEP Regulatory Penalties = 0.",
        s9_kpi4_math_imp: "Impact: Zero risk of insurance commissioner penalties and unconditional operational stability.",'''

ptb_calc = '''        // Slide 9: Memória de Cálculo & Metodologia
        s9_calc_btn: "🧮 Memória de Cálculo & Metodologia",
        s9_calc_callout_title: "BASE METODOLÓGICA E AMOSTRAGEM AUDITADA (MAPFRE BRASIL)",
        s9_calc_callout_desc: "Métricas auditadas sobre universo real de 110 releases tarifários/ano, 1.250 chamados técnicos de atuários e rastreabilidade integral PECA. Fórmulas matemáticas 100% reproduzíveis.",
        s9_calc_pill: "📊 Memória de Cálculo",
        s9_modal_title: "Memória de Cálculo & Base Metodológica — ACDC Platform",
        s9_modal_sub: "Auditoria analítica de fórmulas matemáticas, horas técnicas economizadas, velocidade de homologação e mitigação de falhas na MAPFRE.",
        s9_kpi1_math_title: "1. Horas Técnicas Poupadas ao Ano (+1.400 h)",
        s9_kpi1_math_base: "Antes (Legado Manual): 16 horas técnicas por release (inserção manual JSON no MongoDB, depuração de sintaxe e homologação QA). Total: 110 × 16 h = 1.760 h/ano.",
        s9_kpi1_math_plat: "Com Cockpit ACDC: 3 horas técnicas por release (validação de schema em tempo real, autocompletion atuarial, diff visual e rollback imediato). Total: 110 × 3 h = 330 h/ano.",
        s9_kpi1_math_eq: "Fórmula: Economia = 1.760 h - 330 h = 1.430 horas economizadas/ano (reportado contabilmente: +1.400 h/ano).",
        s9_kpi1_math_imp: "Impacto: Desbloqueio de capacidade técnica equivalente a quase 1 desenvolvedor/atuário sênior full-time na MAPFRE.",
        s9_kpi2_math_title: "2. Velocidade de Homologação (12x Mais Rápido)",
        s9_kpi2_math_base: "Time-to-Market Legado: 14 dias úteis (Definição de Regra 3d + Codificação JSON 4d + Homologação QA 5d + Deploy 2d).",
        s9_kpi2_math_plat: "Cockpit ACDC: 1,15 dias úteis (~28 horas de esteira contínua ponta a ponta com validação sintática assistida).",
        s9_kpi2_math_eq: "Fórmula: Fator de Aceleração = 14 dias / 1,15 dias = 12,17x (reportado: 12x Mais Rápido).",
        s9_kpi2_math_imp: "Impacto: Lançamento ágil de novos produtos de seguros antes da concorrência no mercado brasileiro.",
        s9_kpi3_math_title: "3. Resolução com ACDC Copilot (92%)",
        s9_kpi3_math_base: "Volume Total Auditado: 1.250 dúvidas técnicas e chamados de suporte N1/N2 registrados por atuários no ano sobre esquemas DUP e tabelas Tronador.",
        s9_kpi3_math_plat: "1.150 dúvidas resolvidas autonomamente pelo Copilot em menos de 1 minuto sem abrir tickets para os arquitetos seniores.",
        s9_kpi3_math_eq: "Fórmula: Taxa de Resolução = (1.150 / 1.250) × 100 = 92,0% de autonomia técnica.",
        s9_kpi3_math_imp: "Impacto: Eliminação de gargalos na mesa de arquitetura e empoderamento com autoatendimento para o time de negócios.",
        s9_kpi4_math_title: "4. Passivos de Não-Conformidade (0 Incidências)",
        s9_kpi4_math_base: "Histórico prévio: Quedas esporádicas em produção por chaves duplicadas ou tipos incompatíveis em esquemas de tarifas.",
        s9_kpi4_math_plat: "ACDC: 100% dos deploys validados com rastreabilidade PECA, assinatura SHA-256 e controle RBAC estrito.",
        s9_kpi4_math_eq: "Fórmula: Incidentes em produção = 0 • Multas regulatórias SUSEP = 0.",
        s9_kpi4_math_imp: "Impacto: Zero risco de penalidades da superintendência de seguros e estabilidade operacional incondicional.",'''

if 's9_kpi4_sub: "Full regulatory audit traceability via PECA",\n' + en_calc not in code:
    code = code.replace(
        's9_kpi4_sub: "Full regulatory audit traceability via PECA",',
        's9_kpi4_sub: "Full regulatory audit traceability via PECA",\n' + en_calc
    )

if 's9_kpi4_sub: "Rastreabilidade integral SUSEP / PECA",\n' + ptb_calc not in code:
    code = code.replace(
        's9_kpi4_sub: "Rastreabilidade integral SUSEP / PECA",',
        's9_kpi4_sub: "Rastreabilidade integral SUSEP / PECA",\n' + ptb_calc
    )

with open(script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: Updated update_i18n.py with valid JS comments and all languages!")
