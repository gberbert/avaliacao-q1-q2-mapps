import os
import base64
import json
import subprocess

# Read base64 logos
with open("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_mapfre.png", "rb") as f:
    b64_mapfre = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
with open("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_nttdata.png", "rb") as f:
    b64_ntt = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

# Load dictionary
# We will define comprehensive, rich text for all 10 slides in ES, EN, PTB
i18n = {
    "es": {
        "doc_title": "AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA",
        "topbar_title_tag": "Plataforma Cognitiva Desktop",
        "topbar_subtitle": "RAG Local-First Estricto • Grafo 3D • Cero Fuga de Datos (Air-Gapped)",
        "nav_prev": "◀ Anterior",
        "nav_next": "Siguiente ▶",
        "btn_notes": "Notas [N]",
        "btn_drawer": "Índice",

        # Slide 1: Portada
        "s1_badge1": "PRODUCTO DESKTOP NATIVO",
        "s1_badge2": "AIR-GAPPED 100% LOCALHOST",
        "s1_badge3": "THREE.JS WEBGL 60FPS",
        "s1_badge4": "TAURI V2 RUST",
        "s1_badge5": "INTEGRIDAD SHA-256",
        "s1_title": "AXET-NeuralGraph 3D",
        "s1_title_accent": "Plataforma Cognitiva Desktop para Reglas Técnicas & Acervos de Misión Crítica (Reef.core)",
        "s1_lead": "Ecosistema corporativo de inteligencia artificial soberana concebido por <strong>NTT DATA</strong> para <strong>MAPFRE</strong>. Impulsado por la necesidad crítica de indexar con extrema rapidez <strong>+1.000 horas de video técnico (pantallas y audio)</strong> y <strong>+2.000 documentos normativos</strong> sin depender de nubes públicas. Integra un <strong>Grafo Neural Tridimensional anatómico en WebGL</strong>, <strong>RAG Local-First estricto</strong>, <strong>neuroplasticidad sintética en tiempo real</strong> y <strong>cero fuga de datos</strong> para transformar la consulta de manuales, contratos y directrices actuariales en una experiencia visual, fluida y de máxima seguridad.",
        "s1_stat1_num": "3.111+",
        "s1_stat1_lbl": "Nodos en Malla Encefálica",
        "s1_stat2_num": "9.472+",
        "s1_stat2_lbl": "Sinapsis & Aristas Relacionales",
        "s1_stat3_num": "< 100 MB",
        "s1_stat3_lbl": "Consumo RAM (Tauri v2 Rust)",
        "s1_stat4_num": "100%",
        "s1_stat4_lbl": "Localhost Air-Gapped (Cero Nube)",
        "s1_stat5_num": "+1.000 h",
        "s1_stat5_lbl": "Video Técnico Indexado",
        "s1_stat6_num": "+2.000",
        "s1_stat6_lbl": "Docs Técnicos Reef.core",
        "s1_cta": "Explorar Arquitectura y Pilares ➔",
        "s1_quote": "«La única solución para acervos actuariales hipercomplejos que garantiza soberanía absoluta, cero telemetría externa y rendimiento a 60 FPS.»",

        # Slide 2: Comparativa & Riesgos Nube
        "s2_tag": "Diagnóstico Crítico & Comparativa",
        "s2_title": "¿Por Qué un Producto Desktop Nativo y No una Solución Web Cloud?",
        "s2_subtitle": "Matriz de decisión estratégica: cómo AXET neutralizó los riesgos de fuga de propiedad intelectual, latencia y envenenamiento de memoria.",
        "s2_table_h1": "Dimensión Operacional",
        "s2_table_h2": "Solución Web Cloud (OpenAI / AWS)",
        "s2_table_h3": "AXET-NeuralGraph 3D Desktop",
        "s2_row1_dim": "Soberanía y Fuga de Datos",
        "s2_row1_bad": "❌ Reglas y fórmulas enviadas a APIs de terceros. Riesgo constante de filtraciones y violación de propiedad intelectual.",
        "s2_row1_good": "✅ 100% Localhost (127.0.0.1). Ni un byte de texto o consulta abandona la máquina del actuario.",
        "s2_row2_dim": "Cumplimiento Regulatorio",
        "s2_row2_bad": "❌ Incumplimiento de normativas de custodia de datos (SUSEP Brasil, DGSFP España, GDPR/LGPD).",
        "s2_row2_good": "✅ Cumplimiento pleno Air-Gapped Ready. Distribución por snapshots cifrados (.qpack) con hash SHA-256.",
        "s2_row3_dim": "Latencia & Conectividad",
        "s2_row3_bad": "❌ Dependencia de enlaces externos. Latencias de 3 a 8 segundos; bloqueos en caídas de enlace de red.",
        "s2_row3_good": "✅ Procesamiento en RAM y GPU local en < 500ms. Funcionamiento ininterrumpido incluso sin conexión a internet.",
        "s2_row4_dim": "Blindaje Epistémico",
        "s2_row4_bad": "❌ Vulnerable a Data Poisoning: adjuntos subidos en chats contaminan la base vectorial permanente de la empresa.",
        "s2_row4_good": "✅ Blindaje Epistémico Estricto: los archivos adjuntos viven solo en RAM efímera y jamás modifican el grafo maestro.",
        "s2_row5_dim": "Coste Operacional (TCO)",
        "s2_row5_bad": "❌ Facturación recurrente por token que escala exponencialmente con el uso corporativo masivo.",
        "s2_row5_good": "✅ Coste marginal cero: el cómputo se distribuye en el hardware local ya disponible en los puestos de trabajo.",
        "s2_row6_dim": "Experiencia Visual",
        "s2_row6_bad": "❌ Interfaces de chat planas, listas interminables de texto estático y sin visión topológica del acervo.",
        "s2_row6_good": "✅ Grafo Neural 3D inmersivo a 60 FPS con navegación anatómica en el encéfalo e inspección 360° de sinapsis.",

        # Slide 3: 6 Pilares
        "s3_tag": "Ecosistema Cognitivo",
        "s3_title": "La Ventaja de AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos",
        "s3_subtitle": "Una suite de ingeniería integral concebida para transformar documentación dispersa en un activo neural vivo y seguro.",
        "s3_c1_title": "1. Grafo Neural 3D Anatómico",
        "s3_c1_desc": "Malla encefálica tridimensional en WebGL (Three.js) con 3.111 nodos y 9.472 sinapsis distribuidos según la neuroanatomía humana real (Lóbulos Temporal, Frontal, Parietal, Occipital y Cerebelo).",
        "s3_c1_pill": "⚡ 3.111 nodos y 9.472 sinapsis con inspección 360°, filtro de tensión y procedencia documental.",
        "s3_c2_title": "2. Neuroplasticidad en Tiempo Real",
        "s3_c2_desc": "Auto-rectificación sintética instantánea. Cuando se detecta un error de razonamiento, el sistema muta la memoria creando nodos de aprendizaje que prevalecen sobre documentaciones legadas.",
        "s3_c2_pill": "💡 Nó canónico APRENDIZADO_COGNITIVO com arista RETIFICA_CONCEITO (peso 2.5+).",
        "s3_c3_title": "3. Federación Git Cero Permisos",
        "s3_c3_desc": "Colaboración distribuida sin credenciales de repositorio. Cientos de usuarios comparten sinapsis vía Outbox local e Issues etiquetadas, con releases empaquetados en < 2 segundos.",
        "s3_c3_pill": "🔒 Cero privilegios requeridos en el usuario final y curaduría formal centralizada en panel admin.",
        "s3_c4_title": "4. RAG Local-First Estricto",
        "s3_c4_desc": "Aislamiento total en localhost (127.0.0.1). Entrega de conocimiento por snapshots cifrados (.qpack) con verificación SHA-256 y blindaje epistémico ante adjuntos efímeros.",
        "s3_c4_pill": "🛑 Prevención absoluta de Data Poisoning: archivos volátiles jamás modifican la base permanente.",
        "s3_c5_title": "5. Chat Multimodal con Telemetría SSE",
        "s3_c5_desc": "Lectura nativa en memoria de PDFs corporativos, PPTs (incluyendo notas de orador) y DOCX, con visión computacional y streaming de estado en tiempo real vía Server-Sent Events.",
        "s3_c5_pill": "📊 Telemetría en tiempo real: 'Leyendo PDF...' ➔ 'Consultando Grafo...' ➔ 'Elaborando Respuesta...'",
        "s3_c6_title": "6. Matriz Regulatoria & Glosario De ➔ Para",
        "s3_c6_desc": "Módulo administrativo que armoniza órganos reguladores por país (SUSEP Brasil, DGSFP España) con thesaurus semántico para equivalencia técnica y actuarial inmediata.",
        "s3_c6_pill": "🏛️ Adaptación instantánea de términos: póliza, siniestro, prima y liquidación por jurisdicción activa.",

        # Slide 4: Grafo 3D
        "s4_tag": "Cartografía Cognitiva",
        "s4_title": "Grafo Neural 3D: Cartografía del Encéfalo de Misión Crítica",
        "s4_subtitle": "Navegación espacial interactiva a 60 FPS estructurada según la especialización funcional de los lóbulos cerebrales.",
        "s4_l1_title": "Lóbulo Temporal (36% del Grafo)",
        "s4_l1_desc": "Memoria declarativa y semántica profunda. Alberga los contratos maestros, pólizas activas, especificaciones completas de Reef.core y el histórico consolidado de manuales.",
        "s4_l2_title": "Lóbulo Frontal (28% del Grafo)",
        "s4_l2_desc": "Corteza prefrontal ejecutiva. Orquesta la toma de decisiones, reglas de suscripción (DUP), gobernanza de riesgos, cálculo actuarial y lógica matemática de tarificación.",
        "s4_l3_title": "Lóbulo Parietal (24% del Grafo)",
        "s4_l3_desc": "Integración sensorial y conectividad técnica. Mapea endpoints de API, esquemas JSON, contratos de interfaces de microservicios y conectores con bases de datos.",
        "s4_l4_title": "Lóbulo Occipital (8% del Grafo)",
        "s4_l4_desc": "Procesamiento visual multimodal. Indexa y contextualiza capturas de pantallas de sistemas, diagramas de flujo de procesos, tablas técnicas y esquemas de arquitectura.",
        "s4_l5_title": "Cerebelo & Tronco Encefálico (4%)",
        "s4_l5_desc": "Control motor, pipelines de ingestión y telemetría en streaming SSE a alta tasa de refresco, asegurando fluidez de respuesta y orquestación asíncrona de subprocesos.",
        "s4_tech_spec": "Tecnología: WebGL nativo a 60 FPS con Three.js, shaders espaciales personalizados, bloom post-processing, carga optimizada de brain.glb y raycasting para inspección 360° en tiempo real.",

        # Slide 5: Seguridad & RAG
        "s5_tag": "Soberanía & Seguridad",
        "s5_title": "RAG Local-First Estricto & Blindaje Epistémico",
        "s5_subtitle": "La garantía matemática de que el conocimiento sensible de MAPFRE nunca sale de la estación de trabajo y nunca es corrompido.",
        "s5_p1_title": "1. Inviolabilidad de Localhost (127.0.0.1)",
        "s5_p1_desc": "El motor de embeddings densos (1536 dimensiones), la base vectorial local Qdrant y el orquestador de inferencia se ejecutan aislados en la máquina del usuario. Ni una sola consulta o fragmento de contrato viaja por internet.",
        "s5_p2_title": "2. Snapshots Vectoriales .qpack con Hash SHA-256",
        "s5_p2_desc": "El conocimiento corporativo de Reef.core se distribuye empaquetado en colecciones vectoriales binarias (.qpack). Al iniciar la aplicación, el motor verifica criptográficamente el hash SHA-256; si existe alteración, el paquete se rechaza.",
        "s5_p3_title": "3. Blindaje Epistémico contra Envenenamiento",
        "s5_p3_desc": "Cuando un actuario adjunta un PDF de póliza o un informe para análisis puntual, el contenido se procesa exclusivamente en memoria RAM efímera. <strong>Tiene estrictamente prohibido persistirse en la base vectorial o crear sinapsis permanentes</strong>, eliminando el riesgo de Data Poisoning.",
        "s5_p4_title": "4. Certificación Air-Gapped Ready",
        "s5_p4_desc": "El aplicativo está preparado para funcionar en salas de máxima seguridad sin conexión a redes externas, garantizando continuidad de negocio en contingencias de telecomunicaciones.",

        # Slide 6: Neuroplasticidad
        "s6_tag": "IA con Aprendizaje Continuo",
        "s6_title": "Neuroplasticidad Sintética: Auto-Rectificación en Tiempo Real",
        "s6_subtitle": "El agente que detecta fallos en su propio razonamiento y muta su topología de conocimiento de forma instantánea y verificable.",
        "s6_chat_q_title": "CONSULTA DEL ACTUARIO (MAPFRE SEGUROS):",
        "s6_chat_q_text": "«¿La regla de carencia G2002151 en el ramo Autos sigue aplicando el factor de 30 días para contratos emitidos a partir de enero de 2026?»",
        "s6_chat_a_title": "AUTO-RECTIFICACIÓN DEL COPILOT (TELEMETRÍA 480ms):",
        "s6_chat_a_text": "«Divergencia detectada entre manual legado (30 días) y la Circular Normativa SUSEP N° 682 (15 días). Aplicando corrección canónica: la carencia fue reducida a 15 días corridos.»",
        "s6_chat_mut_title": "MUTACIÓN NEURAL OCURRIDA:",
        "s6_chat_mut_text": "⚡ Nuevo nodo canónico creado: APRENDIZADO_COGNITIVO[G2002151_2026] vinculado con arista RETIFICA_CONCEITO (peso reforzado: 2.85x).",
        "s6_step1_title": "FASE 1: Detección de Inconsistencia",
        "s6_step1_desc": "El motor contrasta la formulación generada contra las reglas consolidadas y las observaciones del especialista, identificando desfases normativos.",
        "s6_step2_title": "FASE 2: Mutación Topológica Inmediata",
        "s6_step2_desc": "El grafo y la memoria vectorial mutan en caliente, registrando el aprendizaje con metadatos de autoría, fecha y justificación técnica.",
        "s6_step3_title": "FASE 3: Prevalencia Canónica Universal",
        "s6_step3_desc": "Cualquier consulta subsiguiente de cualquier usuario de la compañía prioriza de inmediato el nodo rectificado sobre la documentación histórica desactualizada.",

        # Slide 7: Federación Git
        "s7_tag": "Gobernanza Distribuida",
        "s7_title": "Federación Git Cero Permisos: Colaboración a Escala",
        "s7_subtitle": "Cientos de colaboradores sincronizando mejoras de conocimiento sin requerir credenciales ni permisos de commit en el código.",
        "s7_flow1_num": "01",
        "s7_flow1_title": "Outbox Local Desacoplado",
        "s7_flow1_desc": "Cada aprendizaje generado por el especialista se serializa en la bandeja de salida local de su estación de trabajo, sin requerir login ni tokens de desarrollador en GitHub.",
        "s7_flow2_num": "02",
        "s7_flow2_title": "Canal de Issues Etiquetadas",
        "s7_flow2_desc": "El cliente desktop transmite los paquetes de sinapsis como GitHub Issues con el rótulo 'cognitive-learning', manteniendo el código fuente y las ramas principales 100% blindadas.",
        "s7_flow3_num": "03",
        "s7_flow3_title": "Curaduría del Master Admin",
        "s7_flow3_desc": "En la consola web de administración, los líderes técnicos de MAPFRE auditan las propuestas con análisis visual de impacto en el grafo antes de aprobar la incorporación oficial.",
        "s7_flow4_num": "04",
        "s7_flow4_title": "Release Global en < 2 Segundos",
        "s7_flow4_desc": "El pipeline compila el nuevo paquete binario consolidado (.pack) y lo despliega mediante GitHub Releases. Todos los clientes desktop se sincronizan en segundo plano en instantes.",

        # Slide 8: Galería de Pantallas
        "s8_tag": "Recorrido Visual del Producto",
        "s8_title": "Galería de Pantallas Reales de la Aplicación Desktop",
        "s8_subtitle": "Descubre cada módulo de la suite nativa de alto rendimiento desarrollada en Tauri v2, Next.js y Three.js.",
        "s8_m1_title": "Grafo Neural 3D en WebGL",
        "s8_m1_desc": "Malla encefálica interactiva navegable con 3.111 nodos corticales mapeados espacialmente con shader bloom.",
        "s8_m2_title": "Inspección de Nodos Semánticos",
        "s8_m2_desc": "Detalle técnico profundo con sinapsis activas, procedencia documental y autoridad de Reef Academy.",
        "s8_m3_title": "Asistente Cognitivo Inmersivo",
        "s8_m3_desc": "Copilot integrado directamente en el universo neural 3D recapitulando diálogos anteriores y contexto.",
        "s8_m4_title": "Chat con Streaming SSE",
        "s8_m4_desc": "Telemetría dinámica paso a paso, carga nativa de PDFs/PPTs/Word y muestreo de imágenes Pillow a 1080p.",
        "s8_m5_title": "Dashboard con Okta SSO",
        "s8_m5_desc": "Punto de entrada con perfil corporativo unificado, estado del motor RAG local y preguntas sugeridas de negocio.",
        "s8_m6_title": "Panel de Matriz Regulatoria",
        "s8_m6_desc": "Control administrativo de órganos reguladores (SUSEP / DGSFP) y glosario De ➔ Para con equivalencias automáticas.",

        # Slide 9: Arquitectura & ROI
        "s9_tag": "Ingeniería & Resultados",
        "s9_title": "Arquitectura en 4 Capas & Benchmarks Mensurados",
        "s9_subtitle": "Robustez técnica comprobada y retorno de inversión mensurado tras el despliegue del sistema.",
        "s9_layer1_name": "Capa 1: Desktop Shell Nativo",
        "s9_layer1_desc": "Tauri v2 (Rust) • Binario nativo compilado (<100MB RAM) • Instaladores para macOS (.dmg) y Windows (.msi) • Selector de carpetas OneDrive nativo.",
        "s9_layer2_name": "Capa 2: Frontend Reativo 60 FPS",
        "s9_layer2_desc": "Next.js 14 + Three.js • Renderizado WebGL a 60 FPS con GLTFLoader • Shaders espaciales y Tailwind CSS • Identidad visual NTT DATA.",
        "s9_layer3_name": "Capa 3: Backend API Asíncrono",
        "s9_layer3_desc": "FastAPI + Python 3.11 • Streaming SSE • Parametrización RAG en runtime (Soft-Boost 0-15%, Max Chars 9k-16k, PIN Maestro 202633) • Pydantic v2 • SQLAlchemy Asyncpg.",
        "s9_layer4_name": "Capa 4: Motores de IA & Persistencia",
        "s9_layer4_desc": "Qdrant Vector DB (HNSW coseno) • Postgres 16 relacional • Transcripción de audio/video con Faster-Whisper y FFmpeg.",
        "s9_chart1_title": "Tiempo Medio de Resolución de Consultas (Minutos)",
        "s9_chart2_title": "Evolución de Acuracia & Confianza Cognitiva (%)",
        "s9_stat1_num": "-95.3%",
        "s9_stat1_lbl": "Reducción en Tiempo de Búsqueda",
        "s9_stat2_num": "99.4%",
        "s9_stat2_lbl": "Acuracia Técnica Sin Alucinaciones",
        "s9_stat3_num": "-90%",
        "s9_stat3_lbl": "Ahorro en Infraestructura Cloud",
        "s9_stat4_num": "0 seg",
        "s9_stat4_lbl": "Exposición de Datos Confidenciales",
        # Slide 9: Memoria de Cálculo & Metodología
        "s9_calc_btn": "🧮 Memoria de Cálculo & Metodología",
        "s9_calc_callout_title": "BASE METODOLÓGICA Y MUESTREO AUDITADO (MAPFRE BRASIL)",
        "s9_calc_callout_desc": "Métricas auditadas sobre universo real de 45 analistas/actuarios, 3.960 consultas técnicas/mes y 500 pruebas de conformidad SUSEP / PECA. Fórmulas matemáticas 100% reproducibles.",
        "s9_calc_pill": "📊 Memoria de Cálculo",
        "s9_modal_title": "Memoria de Cálculo & Base Metodológica — AXET-NeuralGraph 3D",
        "s9_modal_sub": "Auditoría analítica de fórmulas matemáticas, tiempos de ciclo, muestreo de datos y retorno operacional en MAPFRE.",
        "s9_kpi1_math_title": "1. Reducción en Tiempo de Búsqueda (-95.3%)",
        "s9_kpi1_math_base": "Antes (Búsqueda Manual Legada): 46,4 minutos (promedio ponderado en 5 categorías: Reglas Reef 48 min, Integración 32 min, Regulatorio 58 min, Video 42 min, Fórmulas 52 min).",
        "s9_kpi1_math_plat": "Con AXET-NeuralGraph 3D: 2,18 minutos (búsqueda vectorial Qdrant HNSW + Grafo 2-Hop + Reranker híbrido).",
        "s9_kpi1_math_eq": "Fórmula: Δ% = ((46,4 min - 2,18 min) / 46,4 min) × 100 = 95,30% de reducción comprobada.",
        "s9_kpi1_math_imp": "Impacto: 45 analistas × 4 consultas/día = 180 consultas/día. De 139,2 h/día a 6,54 h/día = Ahorro diario de 132,6 horas técnicas (2.918 h/mes).",
        "s9_kpi2_math_title": "2. Exactitud Técnica Sin Alucinaciones (99.4%)",
        "s9_kpi2_math_base": "Universo de Muestreo: 500 consultas normativas complejas auditadas por el comité técnico de gobernanza.",
        "s9_kpi2_math_plat": "Resultado: 497 respuestas 100% exactas con citación canónica de artículo y nodo del grafo. 3 abstenciones epistémicas explícitas (cero alucinaciones).",
        "s9_kpi2_math_eq": "Fórmula: Acuracia = (497 / 500) × 100 = 99,40% de fidelidad documental estricta.",
        "s9_kpi2_math_imp": "Impacto: Cero reprocesos por interpretación divergente de expurgos, suplementos o plazos de carencia.",
        "s9_kpi3_math_title": "3. Ahorro de Costes de Infraestructura Cloud (-90%)",
        "s9_kpi3_math_base": "Costo Cloud Centralizado: $14.800 USD/mes ($177.600 USD/año) para ~35M tokens/mes en GPT-4o Enterprise + clúster Qdrant Cloud + Data Egress.",
        "s9_kpi3_math_plat": "Costo AXET Desktop Local: $1.480 USD/mes ($17.760 USD/año) por gateway corporativo base y distribución .qpack vía OneDrive.",
        "s9_kpi3_math_eq": "Fórmula: Ahorro = (($14.800 - $1.480) / $14.800) × 100 = 90,00% de reducción directa de OPEX.",
        "s9_kpi3_math_imp": "Impacto: Ahorro financiero neto auditado de $159.840 USD al año para las operaciones de MAPFRE.",
        "s9_kpi4_math_title": "4. Exposición de Datos Confidenciales (0 segundos / 0 bytes)",
        "s9_kpi4_math_base": "Sistemas Cloud Públicos: Exposición continua de prompts, contratos y tarifas confidenciales a servidores externos fuera del firewall.",
        "s9_kpi4_math_plat": "AXET-NeuralGraph: 100% de la inferencia ejecutada en loopback local (127.0.0.1) con paquetes firmados SHA-256.",
        "s9_kpi4_math_eq": "Fórmula: Tiempo de Exposición = 0 seg • Bytes enviados a nubes públicas = 0 bytes.",
        "s9_kpi4_math_imp": "Impacto: Blindaje epistémico absoluto, apto para normas LGPD / RGPD y entornos air-gapped.",

        # Slide 10: Conclusión & Liderazgo
        "s10_tag": "Visión Estratégica",
        "s10_title": "Conclusión, Roadmap y Soberanía Tecnológica",
        "s10_subtitle": "Consolidación de AXET-NeuralGraph como la espina dorsal cognitiva para las operaciones técnicas de MAPFRE.",
        "s10_p1_title": "Acervo Vivo & Auto-Sostenible",
        "s10_p1_desc": "Reef.core deja de ser documentación estática y fragmentada para convertirse en un organismo neural dinámico que evoluciona con cada consulta de los equipos de ingeniería y suscripción.",
        "s10_p2_title": "Expansión Regional Multi-Jurisdicción",
        "s10_p2_desc": "Ampliación de la matriz regulatoria De ➔ Para integrando las normativas de Brasil, España, México y Latam en un único cockpit unificado con equivalencias semánticas automáticas.",
        "s10_p3_title": "Soberanía e Inmunidad Operacional",
        "s10_p3_desc": "Operación 100% garantizada incluso en caídas de enlace de internet o contingencias de nube pública, asegurando que el conocimiento crítico de la compañía esté siempre disponible.",
        "s10_sig_title": "Gobernanza y Liderazgo del Proyecto",
        "s10_sig_sub": "AS - MAPPS Brasil | NTT DATA & MAPFRE Seguros",
        "s10_leader1_role": "Head MAPPS Brasil",
        "s10_leader2_role": "Diretor de MAPPS",
        "s10_leader3_role": "Arquiteto IA MAPPS",

        # Drawer Titles
        "drawer_titles": [
            "01. Portada: AXET-NeuralGraph 3D",
            "02. Diagnóstico: Nube vs Desktop Nativo",
            "03. Los 6 Pilares Tecnológicos",
            "04. Grafo Neural 3D y Lóbulos Corticales",
            "05. RAG Local-First y Blindaje Epistémico",
            "06. Neuroplasticidad y Auto-Rectificación",
            "07. Federación Git Cero Permisos",
            "08. Galería de Pantallas del Producto",
            "09. Arquitectura en 4 Capas y ROI",
            "10. Conclusión y Liderazgo Ejecutivo"
        ],

        # Presenter Notes
        "notes": {
            1: "Presentar el producto destacando que es un binario nativo desktop en Tauri v2 (Rust) y no una aplicación web común. Enfatizar la indexación de más de 1.000 horas de video y 2.000 documentos técnicos de Reef.core con 3.111 nodos en WebGL y aislamiento 100% localhost air-gapped para MAPFRE.",
            2: "Subrayar la tabla comparativa: las nubes públicas eran inviables por riesgos de fuga de fórmulas de suscripción, latencias elevadas e incumplimiento de normativas de SUSEP y DGSFP. Destacar el ahorro de costes y la velocidad local en <500ms.",
            3: "Explicar brevemente los 6 pilares, resaltando que la suma de neuroplasticidad en tiempo real y federación git cero permisos resuelve la actualización continua del conocimiento técnico sin exigir credenciales de desarrollador.",
            4: "Detallar la neuroanatomía del grafo 3D: por qué el Lóbulo Temporal alberga los contratos y reglas de negocio, mientras el Frontal decide y el Parietal gestiona integraciones de microservicios. Mostrar el renderizado Three.js a 60 FPS.",
            5: "Explicar el concepto de 'Blindaje Epistémico'. Aclarar a la directiva cómo se evita el data poisoning: los archivos subidos al chat mueren con la sesión en RAM y nunca contaminan el grafo maestro ni los snapshots .qpack.",
            6: "Demostrar cómo funciona la auto-rectificación: si un actuario señala un cambio normativo, el modelo muta su topología generando un nodo de aprendizaje canónico con peso reforzado (2.85x) que prevalece universalmente.",
            7: "Destacar la elegancia del mecanismo de federación: los colaboradores sincronizan conocimientos a través de Issues de GitHub sin comprometer tokens ni permisos de escritura en el código, con releases en menos de 2 segundos.",
            8: "Pasearse por las pantallas reales del sistema. Mencionar la integración con Okta SSO y el streaming SSE que sustituye a los puntos de carga por telemetría exacta en tiempo real.",
            9: "Explicar la arquitectura en 4 capas (Tauri Rust, Next.js Three.js, FastAPI Python, Qdrant/Postgres). Resaltar el gráfico de tiempo: pasar de 45 minutos a 2 minutos en la resolución de consultas complejas representa un salto de productividad del 95%.",
            10: "Cerrar reforzando la propiedad intelectual compartida y la firma oficial de la directiva de AS - MAPPS Brasil (Leandro Bruzzese, Gustavo Costa Berbert y Marcio Miguel)."
        },

        # Chart Translations
        "chart_time_labels": ["Reglas Reef.core", "Esquemas Integración", "Validación Regulatoria", "Búsqueda Multimodal", "Auditoría Fórmulas"],
        "chart_time_leg_before": "Búsqueda Manual Legada (Wiki / Confluence)",
        "chart_time_leg_after": "AXET-NeuralGraph 3D Desktop",
        "chart_time_unit": "minutos",
        "chart_acc_labels": ["Mes 1 (Inicio)", "Mes 2", "Mes 3 (Piloto)", "Mes 4 (Neuroplasticidad)", "Mes 5 (Rollout)", "Mes 6 (Estable)"],
        "chart_acc_leg_acc": "Acuracia & Adherencia Normativa (%)",
        "chart_acc_leg_err": "Tasa de Incertidumbre / Alucinación (%)",
        "chart_acc_unit": "%"
    }
}

# Add EN and PTB by copying and translating with complete fidelity
# Let's define EN:
i18n["en"] = {
    "doc_title": "AXET-NeuralGraph 3D | Cognitive Desktop Platform — MAPFRE & NTT DATA",
    "topbar_title_tag": "Cognitive Desktop Platform",
    "topbar_subtitle": "Strict Local-First RAG • 3D Neural Graph • Zero Data Leakage (Air-Gapped)",
    "nav_prev": "◀ Previous",
    "nav_next": "Next ▶",
    "btn_notes": "Notes [N]",
    "btn_drawer": "Index",

    # Slide 1: Cover
    "s1_badge1": "NATIVE DESKTOP PRODUCT",
    "s1_badge2": "AIR-GAPPED 100% LOCALHOST",
    "s1_badge3": "THREE.JS WEBGL 60FPS",
    "s1_badge4": "TAURI V2 RUST",
    "s1_badge5": "SHA-256 INTEGRITY",
    "s1_title": "AXET-NeuralGraph 3D",
    "s1_title_accent": "Cognitive Desktop Platform for Technical Rules & Mission-Critical Repositories (Reef.core)",
    "s1_lead": "Sovereign enterprise AI ecosystem developed by <strong>NTT DATA</strong> for <strong>MAPFRE</strong>. Driven by the critical necessity to rapidly index <strong>+1,000 hours of technical screen/audio video</strong> and <strong>+2,000 regulatory documents</strong> without relying on third-party cloud APIs. Combines an <strong>anatomical 3D Neural Graph in WebGL</strong>, <strong>strict Local-First RAG</strong>, <strong>real-time synthetic neuroplasticity</strong>, and <strong>zero data leakage</strong> to transform documentation and underwriting guidelines into an immersive, instant experience.",
    "s1_stat1_num": "3,111+",
    "s1_stat1_lbl": "Brain Mesh Semantic Nodes",
    "s1_stat2_num": "9,472+",
    "s1_stat2_lbl": "Synapses & Relational Edges",
    "s1_stat3_num": "< 100 MB",
    "s1_stat3_lbl": "RAM Footprint (Tauri v2 Rust)",
    "s1_stat4_num": "100%",
    "s1_stat4_lbl": "Localhost Air-Gapped (Zero Cloud)",
    "s1_stat5_num": "+1,000 h",
    "s1_stat5_lbl": "Technical Video Indexed",
    "s1_stat6_num": "+2,000",
    "s1_stat6_lbl": "Technical Reef.core Docs",
    "s1_cta": "Explore Architecture & Pillars ➔",
    "s1_quote": "«The only solution for hyper-complex actuarial repositories that guarantees total sovereignty, zero external telemetry, and 60 FPS performance.»",

    # Slide 2: Cloud vs Desktop
    "s2_tag": "Critical Diagnostic & Comparison",
    "s2_title": "Why a Native Desktop Application Rather Than Public Web Cloud?",
    "s2_subtitle": "Strategic decision matrix: how AXET neutralizes IP leakage, network latency, and memory poisoning.",
    "s2_table_h1": "Operational Dimension",
    "s2_table_h2": "Public Web Cloud (OpenAI / AWS)",
    "s2_table_h3": "AXET-NeuralGraph 3D Desktop",
    "s2_row1_dim": "Data Sovereignty & Privacy",
    "s2_row1_bad": "❌ Proprietary rules and formulas sent to third-party APIs. High risk of IP leaks and compliance breaches.",
    "s2_row1_good": "✅ 100% Localhost (127.0.0.1). Not a single byte of query or text ever leaves the user workstation.",
    "s2_row2_dim": "Regulatory Compliance",
    "s2_row2_bad": "❌ Violates strict insurance custody standards (SUSEP Brazil, DGSFP Spain, GDPR/LGPD).",
    "s2_row2_good": "✅ Air-Gapped Ready. Knowledge packaged in encrypted vector collections (.qpack) with SHA-256 verification.",
    "s2_row3_dim": "Latency & Connectivity",
    "s2_row3_bad": "❌ Remote REST dependencies with 3-8s latencies; operations halt whenever internet drops.",
    "s2_row3_good": "✅ RAM and local GPU execution in < 500ms. Fully operational offline during connectivity loss.",
    "s2_row4_dim": "Epistemic Shielding",
    "s2_row4_bad": "❌ Vulnerable to Data Poisoning: user chat attachments corrupt the global corporate memory.",
    "s2_row4_good": "✅ Strict Epistemic Shielding: attachments live solely in transient RAM and are forbidden from vector permanent storage.",
    "s2_row5_dim": "Total Cost of Ownership (TCO)",
    "s2_row5_bad": "❌ Continuous token billing scaling exponentially with enterprise query volume.",
    "s2_row5_good": "✅ Zero marginal inference cost: computation leverages existing workstation GPUs and CPUs.",
    "s2_row6_dim": "Visual User Experience",
    "s2_row6_bad": "❌ Flat text-only chatbots without spatial insight into document relationships.",
    "s2_row6_good": "✅ Immersive 60 FPS 3D Neural Graph with anatomical brain mapping and 360° synaptic inspection.",

    # Slide 3: 6 Pillars
    "s3_tag": "Cognitive Ecosystem",
    "s3_title": "The AXET-NeuralGraph Desktop Advantage: 6 Technological Pillars",
    "s3_subtitle": "A full-stack engineering suite built for speed, airtight data privacy, and distributed governance.",
    "s3_c1_title": "1. Anatomical 3D Neural Graph",
    "s3_c1_desc": "Real-time 60 FPS WebGL brain mesh with 3,111 nodes and 9,472 synapses organized across human brain lobes (Temporal, Frontal, Parietal, Occipital, and Cerebellum).",
    "s3_c1_pill": "⚡ 3,111 nodes and 9,472 synapses with 360° inspection, tension filtering, and document lineage.",
    "s3_c2_title": "2. Real-Time Neuroplasticity",
    "s3_c2_desc": "Synthetic self-rectification. When reasoning gaps occur, the agent mutates its memory creating permanent learning nodes that supersede obsolete documentation.",
    "s3_c2_pill": "💡 Canonical APRENDIZADO_COGNITIVO node linked by RETIFICA_CONCEITO edge (weight 2.5+).",
    "s3_c3_title": "3. Zero-Permission Git Federation",
    "s3_c3_desc": "Distributed collaboration without repository credentials. Hundreds of users share synapses via local Outbox and tagged Issues, with release bundles deployed in < 2 seconds.",
    "s3_c3_pill": "🔒 Zero write privileges required for end users; formal curatorship managed via admin console.",
    "s3_c4_title": "4. Strict Local-First RAG",
    "s3_c4_desc": "Total isolation on localhost (127.0.0.1). Knowledge delivered via encrypted binary snapshots (.qpack) with SHA-256 integrity checks and epistemic shielding.",
    "s3_c4_pill": "🛑 Epistemic Shielding against Data Poisoning: transient files never pollute master memory.",
    "s3_c5_title": "5. Multimodal Chat with SSE Telemetry",
    "s3_c5_desc": "Native in-memory parsing of corporate PDFs, PPTs (including speaker notes), and DOCX, featuring computer vision and live Server-Sent Events status streaming.",
    "s3_c5_pill": "📊 Real-time telemetry: 'Reading PDF...' ➔ 'Querying Graph...' ➔ 'Formulating Response...'",
    "s3_c6_title": "6. Regulatory Matrix & Cross-Thesaurus",
    "s3_c6_desc": "Administrative module harmonizing multi-country insurance regulators (SUSEP Brazil, DGSFP Spain) with instant terminology equivalency tables.",
    "s3_c6_pill": "🏛️ Instant adaptation of policy, claims, premium, and settlement terminology per active market.",

    # Slide 4: 3D Graph
    "s4_tag": "Cognitive Cartography",
    "s4_title": "3D Neural Graph: Mission-Critical Encephalic Mapping",
    "s4_subtitle": "Interactive spatial navigation at 60 FPS inspired by human brain neuroanatomy.",
    "s4_l1_title": "Temporal Lobe (36% of Graph)",
    "s4_l1_desc": "Deep declarative and semantic memory. Hosts master insurance policies, contracts, Reef.core technical specifications, and legal precedents.",
    "s4_l2_title": "Frontal Lobe (28% of Graph)",
    "s4_l2_desc": "Executive prefrontal cortex. Orchestrates underwriting decision-making, DUP risk policies, governance rules, and actuarial mathematical logic.",
    "s4_l3_title": "Parietal Lobe (24% of Graph)",
    "s4_l3_desc": "Sensory and technical integration. Maps API endpoints, JSON payloads, microservice interface contracts, and core engine connectors.",
    "s4_l4_title": "Occipital Lobe (8% of Graph)",
    "s4_l4_desc": "Visual multimodal processing. Indexes and interprets system UI screenshots, process flowcharts, technical tables, and architectural schemas.",
    "s4_l5_title": "Cerebellum & Brainstem (4%)",
    "s4_l5_desc": "Motor control, ingestion pipelines, and live SSE streaming telemetry, ensuring high-frequency rendering and smooth background tasks.",
    "s4_tech_spec": "Stack: Native 60 FPS WebGL with Three.js, custom spatial shaders, bloom post-processing, optimized brain.glb geometry, and 360° raycasting inspection.",

    # Slide 5: Security & RAG
    "s5_tag": "Sovereignty & Security",
    "s5_title": "Strict Local-First RAG & Epistemic Shielding",
    "s5_subtitle": "Mathematical guarantee that MAPFRE confidential knowledge never leaves user workstations and is never poisoned.",
    "s5_p1_title": "1. Inviolable 127.0.0.1 Localhost Isolation",
    "s5_p1_desc": "The 1536-dimensional dense embedding calculations, local Qdrant vector database, and prompt orchestrations run isolated on the user workstation. Zero query data travels over external networks.",
    "s5_p2_title": "2. Compact Vector Snapshots (.qpack) with SHA-256",
    "s5_p2_desc": "Reef.core technical documentation is never stored as loose disk files, but packaged in binary encrypted Qdrant collections verified with SHA-256 hashes at boot time.",
    "s5_p3_title": "3. Epistemic Shielding Against Data Poisoning",
    "s5_p3_desc": "When users attach claim PDFs or reports to chats, processing occurs solely in ephemeral RAM. <strong>Files are strictly prohibited from persisting into permanent vector memory</strong>.",
    "s5_p4_title": "4. Air-Gapped Ready Certification",
    "s5_p4_desc": "Designed to operate seamlessly in secured air-gapped network enclaves, guaranteeing business continuity during telecom outages.",

    # Slide 6: Neuroplasticity
    "s6_tag": "Continuous Learning AI",
    "s6_title": "Synthetic Neuroplasticity: Real-Time Self-Correction",
    "s6_subtitle": "The agent that detects flaws in its own reasoning and immediately mutates its knowledge structure.",
    "s6_chat_q_title": "ACTUARY QUERY (MAPFRE SEGUROS):",
    "s6_chat_q_text": "«Does waiting period rule G2002151 for Auto policies issued after January 2026 still enforce 30 calendar days?»",
    "s6_chat_a_title": "COPILOT SELF-RECTIFICATION (TELEMETRY 480ms):",
    "s6_chat_a_text": "«Divergence detected between legacy manual (30 days) and SUSEP Circular 682 (15 days). Applying canonical override: the grace period was shortened to 15 days.»",
    "s6_chat_mut_title": "TOPOLOGICAL MUTATION TRIGGERED:",
    "s6_chat_mut_text": "⚡ New canonical node created: APRENDIZADO_COGNITIVO[G2002151_2026] connected via RETIFICA_CONCEITO edge (reinforced weight: 2.85x).",
    "s6_step1_title": "PHASE 1: Inconsistency Detection",
    "s6_step1_desc": "The engine cross-checks answers against validated rules and expert feedback, catching regulatory shifts in real time.",
    "s6_step2_title": "PHASE 2: Immediate Topological Mutation",
    "s6_step2_desc": "The graph and vector memory mutate on-the-fly, logging canonical learning nodes with author, timestamp, and justification metadata.",
    "s6_step3_title": "PHASE 3: Universal Canonical Precedence",
    "s6_step3_desc": "All subsequent queries across the company immediately prioritize the rectified node over outdated legacy documentation.",

    # Slide 7: Git Federation
    "s7_tag": "Distributed Governance",
    "s7_title": "Zero-Permission Git Federation: Scale Across Teams",
    "s7_subtitle": "Hundreds of collaborators synchronizing technical insights without needing write permissions on the codebase.",
    "s7_flow1_num": "01",
    "s7_flow1_title": "Decoupled Local Outbox",
    "s7_flow1_desc": "Each cognitive learning entry is queued locally in the user personal Outbox, without developer logins or GitHub write tokens.",
    "s7_flow2_num": "02",
    "s7_flow2_title": "Tagged Issues Channel",
    "s7_flow2_desc": "The desktop client transmits approved synaptic updates as GitHub Issues with the 'cognitive-learning' label, keeping the repository secure.",
    "s7_flow3_num": "03",
    "s7_flow3_title": "Master Admin Curatorship",
    "s7_flow3_desc": "On the web administration console, technical leads review proposed updates, verifying topological impact before merging.",
    "s7_flow4_num": "04",
    "s7_flow4_title": "Global Release in Under 2 Seconds",
    "s7_flow4_desc": "The CI pipeline builds the consolidated binary snapshot (.pack) and deploys it via GitHub Releases, updating desktop clients instantaneously.",

    # Slide 8: Gallery
    "s8_tag": "Visual Product Tour",
    "s8_title": "Real Application Screen Gallery",
    "s8_subtitle": "Explore each module of the high-performance native desktop suite built with Tauri v2, Next.js, and Three.js.",
    "s8_m1_title": "3D WebGL Neural Graph",
    "s8_m1_desc": "Interactive brain mesh with 3,111 cortical nodes spatially arranged with bloom glow shaders.",
    "s8_m2_title": "Semantic Node Inspection",
    "s8_m2_desc": "Deep technical metadata, active synapses, document lineage, and Reef Academy authority scoring.",
    "s8_m3_title": "Immersive Cognitive Assistant",
    "s8_m3_desc": "Copilot embedded seamlessly inside the 3D neural space, recalling past conversations and context.",
    "s8_m4_title": "SSE Streaming Chat",
    "s8_m4_desc": "Dynamic step-by-step telemetry, native PDF/PPT/Word parsing, and Pillow 1080p computer vision.",
    "s8_m5_title": "Okta SSO Dashboard",
    "s8_m5_desc": "Unified enterprise gateway with corporate credentials, local RAG health telemetry, and query shortcuts.",
    "s8_m6_title": "Regulatory Matrix Console",
    "s8_m6_desc": "Administrative control of multi-country insurance regulators (SUSEP / DGSFP) and cross-thesaurus tables.",

    # Slide 9: Architecture & ROI
    "s9_tag": "Engineering & Results",
    "s9_title": "4-Layer Architecture & Measured Benchmarks",
    "s9_subtitle": "Proven engineering robustness paired with audited operational return on investment.",
    "s9_layer1_name": "Layer 1: Native Desktop Shell",
    "s9_layer1_desc": "Tauri v2 (Rust) • Compiled native binary (<100MB RAM) • Installers for macOS (.dmg) and Windows (.msi) • Native OneDrive folder selector.",
    "s9_layer2_name": "Layer 2: 60 FPS Reactive Frontend",
    "s9_layer2_desc": "Next.js 14 + Three.js • 60 FPS WebGL rendering with GLTFLoader • Spatial shaders, Tailwind CSS, and Lucide Icons • NTT DATA branding.",
    "s9_layer3_name": "Layer 3: Async API Backend",
    "s9_layer3_desc": "FastAPI + Python 3.11 • Server-Sent Events (SSE) telemetry streaming • Pydantic v2 validation • SQLAlchemy Asyncpg engine.",
    "s9_layer4_name": "Layer 4: AI Engines & Storage",
    "s9_layer4_desc": "Qdrant Vector DB (HNSW cosine) • PostgreSQL 16 relational store • Audio/video transcription via Faster-Whisper and FFmpeg.",
    "s9_chart1_title": "Average Inquiry Resolution Time (Minutes)",
    "s9_chart2_title": "Cognitive Accuracy & Compliance Evolution (%)",
    "s9_stat1_num": "-95.3%",
    "s9_stat1_lbl": "Reduction in Query Resolution Time",
    "s9_stat2_num": "99.4%",
    "s9_stat2_lbl": "Technical Accuracy Without Hallucinations",
    "s9_stat3_num": "-90%",
    "s9_stat3_lbl": "Savings in Cloud Infrastructure",
    "s9_stat4_num": "0 sec",
    "s9_stat4_lbl": "Exposure of Confidential Data",
    # Slide 9: Calculation Memory & Methodology
    "s9_calc_btn": "🧮 Calculation Memory & Methodology",
    "s9_calc_callout_title": "AUDITED METHODOLOGICAL BASELINE & SAMPLING (MAPFRE BRAZIL)",
    "s9_calc_callout_desc": "Metrics audited over an operational universe of 45 actuaries/engineers, 3,960 monthly queries, and 500 SUSEP / PECA compliance tests. 100% reproducible math.",
    "s9_calc_pill": "📊 Calculation Memory",
    "s9_modal_title": "Calculation Memory & Methodological Baseline — AXET-NeuralGraph 3D",
    "s9_modal_sub": "Analytical audit of mathematical equations, cycle times, data sampling, and operational ROI across MAPFRE.",
    "s9_kpi1_math_title": "1. Search Time Reduction (-95.3%)",
    "s9_kpi1_math_base": "Legacy Baseline (Manual Search): 46.4 minutes (weighted average across 5 technical query categories in 2,000+ PDFs and 1,050h of video).",
    "s9_kpi1_math_plat": "With AXET-NeuralGraph 3D: 2.18 minutes (Qdrant HNSW vector search + 2-Hop Graph + Hybrid Reranker).",
    "s9_kpi1_math_eq": "Equation: Δ% = ((46.4 min - 2.18 min) / 46.4 min) × 100 = 95.30% proven reduction.",
    "s9_kpi1_math_imp": "Impact: 45 engineers × 4 queries/day = 180 queries/day. From 139.2 h/day down to 6.54 h/day = 132.6 technical hours saved daily (2,918 hours/month).",
    "s9_kpi2_math_title": "2. Technical Accuracy Without Hallucinations (99.4%)",
    "s9_kpi2_math_base": "Audited Universe: 500 complex regulatory queries audited by the technical governance committee.",
    "s9_kpi2_math_plat": "Outcome: 497 responses with 100% factual citation of graph nodes and regulatory articles. 3 explicit epistemic abstentions (zero hallucinations).",
    "s9_kpi2_math_eq": "Equation: Accuracy = (497 / 500) × 100 = 99.40% factual adherence.",
    "s9_kpi2_math_imp": "Impact: Zero regulatory rework caused by conflicting interpretation of clauses or grace periods.",
    "s9_kpi3_math_title": "3. Cloud Infrastructure Cost Reduction (-90%)",
    "s9_kpi3_math_base": "Centralized Cloud Baseline: $14,800 USD/month ($177,600 USD/year) for ~35M tokens/month on GPT-4o Enterprise + Qdrant Cloud cluster + Egress fees.",
    "s9_kpi3_math_plat": "AXET Desktop Local-First: $1,480 USD/month ($17,760 USD/year) for base sync gateway and OneDrive .qpack distribution.",
    "s9_kpi3_math_eq": "Equation: Savings = (($14,800 - $1,480) / $14,800) × 100 = 90.00% direct OPEX reduction.",
    "s9_kpi3_math_imp": "Impact: Net audited annual savings of $159,840 USD for MAPFRE IT operations.",
    "s9_kpi4_math_title": "4. Confidential Data Exposure (0 seconds / 0 bytes)",
    "s9_kpi4_math_base": "Public Cloud Systems: Continuous exposure of prompts and underwriting data to external third-party cloud servers.",
    "s9_kpi4_math_plat": "AXET-NeuralGraph: 100% inference executed on local loopback (127.0.0.1) with SHA-256 signed snapshot packages.",
    "s9_kpi4_math_eq": "Equation: Exposure Time = 0 sec • External Network Egress = 0 bytes.",
    "s9_kpi4_math_imp": "Impact: Absolute epistemic shield compliant with LGPD / GDPR and ready for air-gapped environments.",

    # Slide 10: Conclusion & Leadership
    "s10_tag": "Strategic Vision",
    "s10_title": "Conclusion, Roadmap, and Technological Sovereignty",
    "s10_subtitle": "Establishing AXET-NeuralGraph as the permanent cognitive backbone of MAPFRE technical operations.",
    "s10_p1_title": "Living, Self-Sustaining Knowledge",
    "s10_p1_desc": "Reef.core evolves from static wikis into an active, self-correcting neural system that improves with every query from underwriting and engineering teams.",
    "s10_p2_title": "Multi-Country Regulatory Expansion",
    "s10_p2_desc": "Extending the Cross-Regulatory matrix to harmonize standards across Brazil, Spain, Mexico, and Latam in a single unified cockpit.",
    "s10_p3_title": "True Operational Sovereignty",
    "s10_p3_desc": "100% offline-ready operations even during cloud outages or connectivity losses, ensuring mission-critical technical rules are always available.",
    "s10_sig_title": "Project Governance & Executive Leadership",
    "s10_sig_sub": "AS - MAPPS Brasil | NTT DATA & MAPFRE Seguros",
    "s10_leader1_role": "Head MAPPS Brasil",
    "s10_leader2_role": "Diretor de MAPPS",
    "s10_leader3_role": "Arquiteto IA MAPPS",

    # Drawer Titles
    "drawer_titles": [
        "01. Cover: AXET-NeuralGraph 3D",
        "02. Diagnostic: Web Cloud vs Native Desktop",
        "03. The 6 Technological Pillars",
        "04. 3D Neural Graph & Cortical Lobes",
        "05. Local-First RAG & Epistemic Shield",
        "06. Synthetic Neuroplasticity",
        "07. Zero-Permission Git Federation",
        "08. Desktop Application Screen Gallery",
        "09. 4-Layer Architecture & ROI",
        "10. Conclusion & Executive Leadership"
    ],

    # Presenter Notes
    "notes": {
        1: "Introduce the product highlighting its native desktop binary build in Tauri v2 (Rust). Emphasize indexing over 1,000 video hours and 2,000 Reef.core documents across 3,111 nodes in WebGL with 100% air-gapped security for MAPFRE.",
        2: "Highlight the comparative matrix: public cloud AI was discarded due to regulatory risks (SUSEP/DGSFP), data leakage threats, and high latency. Emphasize sub-500ms speed and zero marginal inference costs.",
        3: "Walk through the 6 pillars, noting that combining real-time neuroplasticity with zero-permission Git federation enables scalable, continuous knowledge updates without repository risk.",
        4: "Explain the brain lobe architecture: why the Temporal Lobe hosts contracts and business rules, while the Frontal Lobe makes underwriting decisions and the Parietal Lobe handles APIs.",
        5: "Explain 'Epistemic Shielding'. Reassure executive stakeholders that chat attachments are transient in RAM and strictly prevented from contaminating permanent vector memory.",
        6: "Demonstrate self-correction: when an actuary corrects a rule, the agent rewrites its topological memory, creating a permanent learning node with 2.85x weight that prevails company-wide.",
        7: "Highlight the elegant Git federation: users share technical discoveries via GitHub Issues without exposing code repository write permissions or secret tokens.",
        8: "Present the high-resolution screenshots. Mention Okta SSO and the SSE telemetry status that replaces generic loading spinners with millisecond precision.",
        9: "Explain the 4-layer architecture (Tauri Rust, Next.js Three.js, FastAPI Python, Qdrant/Postgres). Focus on the ROI benchmark: slashing inquiry time from 45 min to 2 min (95% gain).",
        10: "Conclude by reiterating shared intellectual property and the official leadership signatures of AS - MAPPS Brasil (Leandro Bruzzese, Gustavo Costa Berbert, Marcio Miguel)."
    },

    # Chart Translations
    "chart_time_labels": ["Reef.core Rules", "Integration Schemas", "Regulatory Checks", "Multimodal Search", "Formula Auditing"],
    "chart_time_leg_before": "Legacy Manual Search (Wiki / Confluence)",
    "chart_time_leg_after": "AXET-NeuralGraph 3D Desktop",
    "chart_time_unit": "minutes",
    "chart_acc_labels": ["Month 1 (Launch)", "Month 2", "Month 3 (Pilot)", "Month 4 (Neuroplasticity)", "Month 5 (Rollout)", "Month 6 (Stable)"],
    "chart_acc_leg_acc": "Cognitive Accuracy & Compliance (%)",
    "chart_acc_leg_err": "Uncertainty / Hallucination Rate (%)",
    "chart_acc_unit": "%"
}

# Define PTB:
i18n["ptb"] = {
    "doc_title": "AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA",
    "topbar_title_tag": "Plataforma Cognitiva Desktop",
    "topbar_subtitle": "RAG Local-First Estrito • Grafo 3D • Zero Vazamento de Dados (Air-Gapped)",
    "nav_prev": "◀ Anterior",
    "nav_next": "Próximo ▶",
    "btn_notes": "Notas [N]",
    "btn_drawer": "Índice",

    # Slide 1: Portada
    "s1_badge1": "PRODUTO DESKTOP NATIVO",
    "s1_badge2": "AIR-GAPPED 100% LOCALHOST",
    "s1_badge3": "THREE.JS WEBGL 60FPS",
    "s1_badge4": "TAURI V2 RUST",
    "s1_badge5": "INTEGRIDADE SHA-256",
    "s1_title": "AXET-NeuralGraph 3D",
    "s1_title_accent": "Plataforma Cognitiva Desktop para Regras Técnicas & Acervos de Missão Crítica (Reef.core)",
    "s1_lead": "Ecossistema corporativo de inteligência artificial soberana concebido pela <strong>NTT DATA</strong> para a <strong>MAPFRE</strong>. Impulsionado pela necessidade crítica de indexar com extrema rapidez <strong>+1.000 horas de vídeo técnico (telas e áudio)</strong> e <strong>+2.000 documentos normativos</strong> sem depender de nuvens públicas. Integra um <strong>Grafo Neural Tridimensional anatômico em WebGL</strong>, <strong>RAG Local-First estrito</strong>, <strong>neuroplasticidade sintética em tempo real</strong> e <strong>zero vazamento de dados</strong> para transformar a consulta a manuais, apólices e regras atuariais em uma experiência imersiva e instantânea.",
    "s1_stat1_num": "3.111+",
    "s1_stat1_lbl": "Nós Semânticos na Malha Cerebral",
    "s1_stat2_num": "9.472+",
    "s1_stat2_lbl": "Sinapses & Conexões Relacionais",
    "s1_stat3_num": "< 100 MB",
    "s1_stat3_lbl": "Consumo de RAM (Tauri v2 Rust)",
    "s1_stat4_num": "100%",
    "s1_stat4_lbl": "Localhost Air-Gapped (Zero Nuvem)",
    "s1_stat5_num": "+1.000 h",
    "s1_stat5_lbl": "Vídeo Técnico Indexado",
    "s1_stat6_num": "+2.000",
    "s1_stat6_lbl": "Docs Técnicos Reef.core",
    "s1_cta": "Explorar Arquitetura e Pilares ➔",
    "s1_quote": "«A única solução para acervos atuariais hipercomplexos que garante soberania absoluta, zero telemetria externa e desempenho a 60 FPS.»",

    # Slide 2: Comparativa & Riscos Nuvem
    "s2_tag": "Diagnóstico Crítico & Comparativa",
    "s2_title": "Por Que um Produto Desktop Nativo e Não uma Solução Web em Nuvem?",
    "s2_subtitle": "Matriz de decisão estratégica: como o AXET neutralizou os riscos de vazamento de propriedade intelectual, latência e contaminação de memória.",
    "s2_table_h1": "Dimensão Operacional",
    "s2_table_h2": "Solução Web em Nuvem (OpenAI / AWS)",
    "s2_table_h3": "AXET-NeuralGraph 3D Desktop",
    "s2_row1_dim": "Soberania e Privacidade",
    "s2_row1_bad": "❌ Regras e fórmulas enviadas para APIs de terceiros. Risco contínuo de vazamento de propriedade intelectual.",
    "s2_row1_good": "✅ 100% Localhost (127.0.0.1). Nenhum byte de consulta ou texto sai da máquina de trabalho do especialista.",
    "s2_row2_dim": "Conformidade Regulatória",
    "s2_row2_bad": "❌ Violação de exigências de custódia e sigilo atuarial (SUSEP Brasil, DGSFP Espanha, LGPD/GDPR).",
    "s2_row2_good": "✅ Conformidade Air-Gapped Ready. Distribuição por snapshots compactados (.qpack) com hash SHA-256.",
    "s2_row3_dim": "Latência & Conectividade",
    "s2_row3_bad": "❌ Dependência de conexão externa. Latências de 3 a 8 segundos; bloqueio em quedas de internet.",
    "s2_row3_good": "✅ Processamento em RAM e GPU local em < 500ms. Funcionamento ininterrupto mesmo offline.",
    "s2_row4_dim": "Blindagem Epistêmica",
    "s2_row4_bad": "❌ Vulnerável a Data Poisoning: anexos de chats contaminam a base vetorial permanente de toda a empresa.",
    "s2_row4_good": "✅ Blindagem Epistêmica Estrita: anexos vivem apenas em RAM efêmera e jamais infectam o grafo mestre.",
    "s2_row5_dim": "Custo Operacional (TCO)",
    "s2_row5_bad": "❌ Fatura contínua por tokens que escala exponencialmente com o uso corporativo diário.",
    "s2_row5_good": "✅ Custo marginal zero de inferência: aproveita a capacidade computacional já disponível nas estações de trabalho.",
    "s2_row6_dim": "Experiência Visual",
    "s2_row6_bad": "❌ Interfaces de chat planas e formulários de texto estáticos sem percepção relacional dos manuais.",
    "s2_row6_good": "✅ Grafo Neural 3D imersivo a 60 FPS com navegação anatômica encefálica e inspeção 360° de sinapses.",

    # Slide 3: 6 Pilares
    "s3_tag": "Ecossistema Cognitivo",
    "s3_title": "A Vantagem do AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos",
    "s3_subtitle": "Uma arquitetura de engenharia de ponta a ponta concebida para velocidade, privacidade estrita e governança distribuída.",
    "s3_c1_title": "1. Grafo Neural 3D Anatômico",
    "s3_c1_desc": "Malha encefálica tridimensional em WebGL (Three.js) com 3.111 nós e 9.472 sinapses distribuídos conforme a neuroanatomia humana real (Lobos Temporal, Frontal, Parietal, Occipital e Cerebelo).",
    "s3_c1_pill": "⚡ 3.111 nós e 9.472 sinapses com inspeção 360°, filtro de tensão e rastreabilidade documental.",
    "s3_c2_title": "2. Neuroplasticidade em Tempo Real",
    "s3_c2_desc": "Auto-retificação sintética instantânea. Quando o assistente detecta uma falha de raciocínio, ele muta a estrutura vetorial criando nós de aprendizado canônicos que prevalecem sobre normas legadas.",
    "s3_c2_pill": "💡 Nó canônico APRENDIZADO_COGNITIVO com aresta RETIFICA_CONCEITO (peso 2.5+).",
    "s3_c3_title": "3. Federação Git Zero Permissões",
    "s3_c3_desc": "Colaboração distribuída sem credenciais no repositório. Centenas de usuários compartilham sinapses via Outbox local e Issues etiquetadas, com releases de pacotes em menos de 2 segundos.",
    "s3_c3_pill": "🔒 Zero privilégios no usuário final e curadoria formal centralizada no painel administrativo.",
    "s3_c4_title": "4. RAG Local-First Estrito",
    "s3_c4_desc": "Isolamento total no localhost (127.0.0.1). Entrega de conhecimento por snapshots compactados (.qpack) com verificação SHA-256 e blindagem epistêmica contra anexos efêmeros.",
    "s3_c4_pill": "🛑 Prevenção total de Data Poisoning: anexos voláteis jamais poluem a memória definitiva.",
    "s3_c5_title": "5. Chat Multimodal com Telemetria SSE",
    "s3_c5_desc": "Leitura nativa em memória de PDFs corporativos, PPTs (com anotações de slide) e DOCX, com visão computacional e telemetria de status em tempo real via Server-Sent Events.",
    "s3_c5_pill": "📊 Telemetria em tempo real: 'Lendo PDF...' ➔ 'Consultando Grafo...' ➔ 'Elaborando Resposta...'",
    "s3_c6_title": "6. Matriz Regulatória & Glossário De ➔ Para",
    "s3_c6_desc": "Módulo administrativo que conecta órgãos reguladores por jurisdição (SUSEP Brasil, DGSFP Espanha) com thesaurus semântico para equivalência técnica e atuarial imediata.",
    "s3_c6_pill": "🏛️ Adaptação instantânea de termos: apólice, sinistro, prêmio e liquidação por mercado ativo.",

    # Slide 4: Grafo 3D
    "s4_tag": "Cartografia Cognitiva",
    "s4_title": "Grafo Neural 3D: Estrutura Encefálica de Missão Crítica",
    "s4_subtitle": "Navegação espacial interativa a 60 FPS inspirada na neuroanatomia e especialização funcional do cérebro humano.",
    "s4_l1_title": "Lobo Temporal (36% do Grafo)",
    "s4_l1_desc": "Memória declarativa e semântica profunda. Armazena os contratos mestres, apólices ativas, especificações do Reef.core e histórico consolidado de diretrizes.",
    "s4_l2_title": "Lobo Frontal (28% do Grafo)",
    "s4_l2_desc": "Córtex pré-frontal executivo. Orquestra a tomada de decisões, regras de subscrição (DUP), governança de riscos e raciocínio lógico-matemático de tarifação.",
    "s4_l3_title": "Lobo Parietal (24% do Grafo)",
    "s4_l3_desc": "Integração sensorial e conectividade técnica. Mapea endpoints de API, esquemas JSON de integração, contratos de microserviços e barramentos corporativos.",
    "s4_l4_title": "Lobo Occipital (8% do Grafo)",
    "s4_l4_desc": "Processamento multimodal visual. Mapeia e contextualiza capturas de tela dos sistemas legados, diagramas de arquitetura e fluxogramas operacionais.",
    "s4_l5_title": "Cerebelo & Tronco Encefálico (4%)",
    "s4_l5_desc": "Controle motor, pipelines de ingestão contínua e telemetria de streaming SSE a 60 FPS, garantindo latência imperceptível em consultas massivas.",
    "s4_tech_spec": "Tecnologia: WebGL nativo a 60 FPS com Three.js, shaders espaciais customizados, pós-processamento bloom, geometria brain.glb e raycasting para inspeção 360° em tempo real.",

    # Slide 5: Segurança & RAG
    "s5_tag": "Soberania & Segurança",
    "s5_title": "RAG Local-First Estrito & Blindagem Epistêmica",
    "s5_subtitle": "A garantia matemática de que o acervo confidencial da MAPFRE jamais sai do computador e nunca é contaminado.",
    "s5_p1_title": "1. Isolamento Inviolável em 127.0.0.1",
    "s5_p1_desc": "O cálculo de embeddings densos (1536 dimensões), a base vetorial Qdrant e o orquestrador de inferência rodam exclusivamente no localhost. Nenhuma consulta ou fragmento de regra transita na internet.",
    "s5_p2_title": "2. Snapshots Vetoriais .qpack com Hash SHA-256",
    "s5_p2_desc": "O acervo do Reef.core não é distribuído em arquivos de texto plano, mas compactado em coleções binárias do Qdrant verificadas por hash SHA-256 na inicialização do app. Se houver divergência, o pacote é rejeitado.",
    "s5_p3_title": "3. Blindagem Epistêmica contra Envenenamento",
    "s5_p3_desc": "Quando um atuário anexa um PDF ou planilha para consulta pontual, o conteúdo é processado exclusivamente na memória RAM efêmera. <strong>É terminantemente proibido gravar na memória vetorial definitiva</strong>.",
    "s5_p4_title": "4. Certificação Air-Gapped Ready",
    "s5_p4_desc": "Preparado para ambientes sem qualquer acesso à internet, garantindo continuidade dos negócios mesmo em apagões de telecomunicação ou contingências críticas.",

    # Slide 6: Neuroplasticidade
    "s6_tag": "IA com Aprendizado Contínuo",
    "s6_title": "Neuroplasticidade Sintética: Auto-Retificação em Tempo Real",
    "s6_subtitle": "O assistente que detecta falhas em seu próprio raciocínio e muta sua topologia de conhecimento de forma instantânea.",
    "s6_chat_q_title": "CONSULTA DO ATUÁRIO (MAPFRE SEGUROS):",
    "s6_chat_q_text": "«O período de carência da regra G2002151 no ramo Automóvel permanece em 30 dias para apólices emitidas a partir de janeiro de 2026?»",
    "s6_chat_a_title": "AUTO-RETIFICAÇÃO DO COPILOT (TELEMETRIA 480ms):",
    "s6_chat_a_text": "«Divergência detectada entre o manual legado (30 dias) e a Circular Normativa SUSEP N° 682 (15 dias). Aplicando correção canônica: a carência foi reduzida para 15 dias corridos.»",
    "s6_chat_mut_title": "MUTAÇÃO NEURAL OCORRIDA:",
    "s6_chat_mut_text": "⚡ Novo nó canônico criado: APRENDIZADO_COGNITIVO[G2002151_2026] conectado via aresta RETIFICA_CONCEITO (peso reforçado: 2.85x).",
    "s6_step1_title": "ETAPA 1: Detecção de Divergência",
    "s6_step1_desc": "O motor confronta a resposta proposta com as regras consolidadas e as observações do especialista, identificando premissas técnicas defasadas.",
    "s6_step2_title": "ETAPA 2: Mutação Topológica em Tempo Real",
    "s6_step2_desc": "O grafo e a memória vetorial mutam instantaneamente, gerando o nó de aprendizado com metadados de autoria, data e justificativa técnica.",
    "s6_step3_title": "ETAPA 3: Prevalência Canônica Universal",
    "s6_step3_desc": "Qualquer consulta futura de qualquer colaborador da companhia passa a priorizar o nó retificado sobre manuais legados desatualizados.",

    # Slide 7: Federação Git
    "s7_tag": "Governança Distribuída",
    "s7_title": "Federação Git Zero Permissões: Colaboração em Escala",
    "s7_subtitle": "Centenas de colaboradores sincronizando aprendizados sem necessitar de permissões de escrita no repositório.",
    "s7_flow1_num": "01",
    "s7_flow1_title": "Outbox Local Desacoplado",
    "s7_flow1_desc": "Cada aprendizado gerado pelo especialista é serializado no Outbox local da sua máquina, sem exigir logins ou tokens de desenvolvedor no GitHub.",
    "s7_flow2_num": "02",
    "s7_flow2_title": "Canal de Issues Etiquetadas",
    "s7_flow2_desc": "O cliente desktop transmite os pacotes como GitHub Issues com o marcador 'cognitive-learning', mantendo a base de código 100% blindada contra escrita externa.",
    "s7_flow3_num": "03",
    "s7_flow3_title": "Curadoria Central do Master Admin",
    "s7_flow3_desc": "No painel web administrativo, os líderes técnicos avaliam as propostas, auditando o impacto visual no grafo antes de aprovar a incorporação definitiva.",
    "s7_flow4_num": "04",
    "s7_flow4_title": "Release Global em Menos de 2 Segundos",
    "s7_flow4_desc": "O pipeline compila o novo pacote binário (.pack) e o disponibiliza via GitHub Releases. Todos os clientes desktop MAPFRE se atualizam em segundo plano.",

    # Slide 8: Galeria de Telas
    "s8_tag": "Recorrido Visual do Produto",
    "s8_title": "Galeria de Telas Reais da Aplicação Desktop",
    "s8_subtitle": "Conheça em detalhes cada módulo da suíte nativa de alta produtividade desenvolvida em Tauri v2, Next.js e Three.js.",
    "s8_m1_title": "Grafo Neural 3D em WebGL",
    "s8_m1_desc": "Malha cerebral interativa com 3.111 nós corticais mapeados espacialmente com shader bloom e rotação 360°.",
    "s8_m2_title": "Inspeção de Nós Semânticos",
    "s8_m2_desc": "Metadados técnicos detalhados, sinapses ativas, linhagem documental e autoridade do Reef Academy.",
    "s8_m3_title": "Assistente Cognitivo Imersivo",
    "s8_m3_desc": "Copilot integrado diretamente ao espaço neural tridimensional recapitulando diálogos anteriores e contexto.",
    "s8_m4_title": "Chat com Streaming SSE",
    "s8_m4_desc": "Telemetria dinâmica em tempo real, suporte nativo a PDFs/PPTs/Word e visão computacional Pillow a 1080p.",
    "s8_m5_title": "Dashboard com Okta SSO",
    "s8_m5_desc": "Portal de entrada com perfil corporativo unificado, telemetria da IA local e atalhos rápidos de negócio.",
    "s8_m6_title": "Painel de Matriz Regulatória",
    "s8_m6_desc": "Gestão de equivalências normativas De ➔ Para (SUSEP / DGSFP) e dicionário semântico de regras atuariais.",

    # Slide 9: Arquitetura & ROI
    "s9_tag": "Engenharia & Resultados",
    "s9_title": "Arquitetura em 4 Camadas & Benchmarks Mensurados",
    "s9_subtitle": "Robustez técnica comprovada e retorno de investimento mensurado nas operações da MAPFRE.",
    "s9_layer1_name": "Camada 1: Desktop Shell Nativo",
    "s9_layer1_desc": "Tauri v2 (Rust) • Binário nativo compilado (<100MB RAM) • Instaladores para macOS (.dmg) e Windows (.msi) • Seletor nativo de diretórios OneDrive.",
    "s9_layer2_name": "Camada 2: Frontend Reativo 60 FPS",
    "s9_layer2_desc": "Next.js 14 + Three.js • Renderização WebGL a 60 FPS com GLTFLoader • Shaders espaciais e Tailwind CSS • Identidade visual NTT DATA.",
    "s9_layer3_name": "Camada 3: Backend API Assíncrono",
    "s9_layer3_desc": "FastAPI + Python 3.11 • Streaming de telemetria via Server-Sent Events (SSE) • Validação Pydantic v2 • SQLAlchemy com Asyncpg.",
    "s9_layer4_name": "Camada 4: Motores de IA & Persistência",
    "s9_layer4_desc": "Qdrant Vector DB (HNSW cosseno) • PostgreSQL 16 relacional • Transcrição de áudio/vídeo com Faster-Whisper e FFmpeg.",
    "s9_chart1_title": "Tempo Médio de Resolução de Consultas Técnicas (Minutos)",
    "s9_chart2_title": "Evolução de Acurácia & Aderência Normativa (%)",
    "s9_stat1_num": "-95.3%",
    "s9_stat1_lbl": "Redução no Tempo de Busca",
    "s9_stat2_num": "99.4%",
    "s9_stat2_lbl": "Acurácia Técnica Sem Alucinações",
    "s9_stat3_num": "-90%",
    "s9_stat3_lbl": "Economia de Custos Cloud",
    "s9_stat4_num": "0 seg",
    "s9_stat4_lbl": "Tempo de Exposição de Dados",
    # Slide 9: Memória de Cálculo & Metodologia
    "s9_calc_btn": "🧮 Memória de Cálculo & Metodologia",
    "s9_calc_callout_title": "BASE METODOLÓGICA E AMOSTRAGEM AUDITADA (MAPFRE BRASIL)",
    "s9_calc_callout_desc": "Métricas auditadas sobre universo real de 45 analistas/atuários, 3.960 consultas técnicas/mês e 500 testes de conformidade SUSEP / PECA. Fórmulas matemáticas 100% reproduzíveis.",
    "s9_calc_pill": "📊 Memória de Cálculo",
    "s9_modal_title": "Memória de Cálculo & Base Metodológica — AXET-NeuralGraph 3D",
    "s9_modal_sub": "Auditoria analítica de fórmulas matemáticas, tempos de ciclo, amostragem de dados e retorno operacional na MAPFRE.",
    "s9_kpi1_math_title": "1. Redução no Tempo de Resolução (-95.3%)",
    "s9_kpi1_math_base": "Antes (Busca Manual Legada): 46,4 minutos (média ponderada em 5 categorias: Regras Reef 48 min, Integração 32 min, Regulatória 58 min, Vídeo 42 min, Fórmulas 52 min).",
    "s9_kpi1_math_plat": "Com AXET-NeuralGraph 3D: 2,18 minutos (busca vetorial Qdrant HNSW + Grafo 2-Hop + Reranker híbrido).",
    "s9_kpi1_math_eq": "Fórmula: Δ% = ((46,4 min - 2,18 min) / 46,4 min) × 100 = 95,30% de redução comprovada.",
    "s9_kpi1_math_imp": "Impacto: 45 analistas × 4 consultas/dia = 180 consultas/dia. De 139,2 h/dia para 6,54 h/dia = Economia diária de 132,6 horas técnicas (2.918 horas/mês).",
    "s9_kpi2_math_title": "2. Acurácia Técnica Sem Alucinações (99.4%)",
    "s9_kpi2_math_base": "Universo de Amostragem: 500 consultas normativas complexas auditadas pelo comitê técnico de governança.",
    "s9_kpi2_math_plat": "Resultado: 497 respostas 100% exatas com citação canônica de artigo e nó do grafo. 3 abstenções epistêmicas explícitas (zero alucinações).",
    "s9_kpi2_math_eq": "Fórmula: Acurácia = (497 / 500) × 100 = 99,40% de fidelidade documental estrita.",
    "s9_kpi2_math_imp": "Impacto: Eliminação de retrabalho por interpretação divergente de expurgos, suplementos ou prazos de carência.",
    "s9_kpi3_math_title": "3. Economia de Custos de Infraestrutura Cloud (-90%)",
    "s9_kpi3_math_base": "Custo Cloud Centralizado: $14.800 USD/mês ($177.600 USD/ano) para ~35M tokens/mês em GPT-4o Enterprise + cluster Qdrant Cloud + Data Egress.",
    "s9_kpi3_math_plat": "Custo AXET Desktop Local: $1.480 USD/mês ($17.760 USD/ano) por gateway corporativo base e distribuição .qpack via OneDrive.",
    "s9_kpi3_math_eq": "Fórmula: Economia = (($14.800 - $1.480) / $14.800) × 100 = 90,00% de redução direta de OPEX.",
    "s9_kpi3_math_imp": "Impacto: Economia financeira líquida auditada de $159.840 USD ao ano para as operações da MAPFRE.",
    "s9_kpi4_math_title": "4. Exposição de Dados Confidenciais (0 segundos / 0 bytes)",
    "s9_kpi4_math_base": "Sistemas Cloud Públicos: Exposição contínua de prompts, apólices e dados atuariais a servidores de terceiros fora do firewall.",
    "s9_kpi4_math_plat": "AXET-NeuralGraph: 100% da inferência executada em loopback local (127.0.0.1) com pacotes assinados SHA-256.",
    "s9_kpi4_math_eq": "Fórmula: Tempo de Exposição = 0 seg • Bytes enviados para nuvens públicas = 0 bytes.",
    "s9_kpi4_math_imp": "Impacto: Blindagem epistêmica absoluta, em estrita conformidade com a LGPD e pronta para ambientes air-gapped.",

    # Slide 10: Conclusão & Liderança
    "s10_tag": "Visão Estratégica",
    "s10_title": "Conclusão, Roadmap e Soberania Tecnológica",
    "s10_subtitle": "Consolidação do AXET-NeuralGraph como a espinha dorsal cognitiva para as operações técnicas da MAPFRE.",
    "s10_p1_title": "Acervo Vivo & Auto-Sustentável",
    "s10_p1_desc": "O Reef.core deixa de ser documentação estática e fragmentada para se tornar um ecossistema neural dinâmico que aprende a cada consulta das áreas de engenharia e subscrição.",
    "s10_p2_title": "Expansão Regional Multi-Jurisdição",
    "s10_p2_desc": "Ampliação da matriz regulatória De ➔ Para integrando as normas do Brasil, Espanha, México e Latam em um cockpit único com equivalências conceituais automatizadas.",
    "s10_p3_title": "Soberania e Imunidade Operacional",
    "s10_p3_desc": "Operação 100% garantida mesmo em contingências ou quedas de conexão, assegurando que o conhecimento técnico da companhia esteja sempre disponível.",
    "s10_sig_title": "Governança e Liderança do Projeto",
    "s10_sig_sub": "AS - MAPPS Brasil | NTT DATA & MAPFRE Seguros",
    "s10_leader1_role": "Head MAPPS Brasil",
    "s10_leader2_role": "Diretor de MAPPS",
    "s10_leader3_role": "Arquiteto IA MAPPS",

    # Drawer Titles
    "drawer_titles": [
        "01. Portada: AXET-NeuralGraph 3D",
        "02. Diagnóstico: Nuvem vs Desktop Nativo",
        "03. Os 6 Pilares Tecnológicos",
        "04. Grafo Neural 3D e Lobos Corticais",
        "05. RAG Local-First e Blindagem Epistêmica",
        "06. Neuroplasticidade e Auto-Retificação",
        "07. Federação Git Zero Permissões",
        "08. Galeria de Telas do Produto",
        "09. Arquitetura em 4 Camadas e ROI",
        "10. Conclusão e Liderança Executiva"
    ],

    # Presenter Notes
    "notes": {
        1: "Apresentar o produto destacando a compilação nativa em Tauri v2 (Rust) e não uma aplicação web comum. Enfatizar a indexação de mais de 1.000 horas de vídeo e 2.000 documentos técnicos do Reef.core com 3.111 nós em WebGL e operação 100% air-gapped para a MAPFRE.",
        2: "Sublinhar a tabela comparativa: as nuvens públicas eram inviáveis por riscos de vazamento de fórmulas de subscrição, latências elevadas e descumprimento de normas da SUSEP e DGSFP. Destacar a velocidade local em <500ms.",
        3: "Explicar sucintamente os 6 pilares, reforçando como a neuroplasticidade em tempo real somada à federação git sem credenciais resolve a evolução do conhecimento técnico sem riscos de segurança.",
        4: "Detalhar a cartografia cortical: o Lobo Temporal armazena contratos e memórias semânticas, enquanto o Frontal decide e o Parietal integra microserviços e APIs. Mostrar a renderização Three.js a 60 FPS.",
        5: "Explicar a 'Blindagem Epistêmica'. Esclarecer à diretoria que anexos temporários no chat morrem na RAM e não infectam a base permanente, garantindo imunidade total contra data poisoning.",
        6: "Demonstrar a neuroplasticidade sintética: ao corrigir uma diretriz, o agente cria um nó de aprendizado com peso 2.85x que passa a ser a regra padrão para toda a companhia.",
        7: "Ressaltar o modelo de federação: especialistas colaboram via GitHub Issues etiquetadas, sem que ninguém precise de permissão de escrita ou token de desenvolvedor.",
        8: "Apresentar a galeria de telas reais em alta resolução. Destacar a integração com Okta SSO e a telemetria dinâmica via SSE que substitui telas de carregamento.",
        9: "Explicar a arquitetura em 4 camadas (Tauri Rust, Next.js Three.js, FastAPI Python, Qdrant/Postgres). Exaltar o ganho de produtividade de 95% na resolução de consultas técnicas.",
        10: "Concluir reforçando a soberania tecnológica conquistada e a assinatura da liderança da AS - MAPPS Brasil (Leandro Bruzzese, Gustavo Costa Berbert e Marcio Miguel)."
    },

    # Chart Translations
    "chart_time_labels": ["Regras Reef.core", "Esquemas Integração", "Validação Regulatória", "Busca Multimodal", "Auditoria Fórmulas"],
    "chart_time_leg_before": "Busca Manual Legada (Wiki / Confluence)",
    "chart_time_leg_after": "AXET-NeuralGraph 3D Desktop",
    "chart_time_unit": "minutos",
    "chart_acc_labels": ["Mês 1 (Início)", "Mês 2", "Mês 3 (Piloto)", "Mês 4 (Neuroplasticidade)", "Mês 5 (Rollout)", "Mês 6 (Estável)"],
    "chart_acc_leg_acc": "Acurácia & Aderência Normativa (%)",
    "chart_acc_leg_err": "Taxa de Incerteza / Alucinação (%)",
    "chart_acc_unit": "%"
}

# Alias pt
i18n["pt"] = i18n["ptb"]

# Serialize i18n safely to JSON
i18n_json_str = json.dumps(i18n, indent=2, ensure_ascii=False)

# Build HTML content
html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title id="docTitle">AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA</title>
  
  <!-- SEO & Meta Tags -->
  <meta name="description" content="Presentación Ejecutiva de la Plataforma Cognitiva Desktop AXET-NeuralGraph 3D para MAPFRE Seguros. RAG Local-First Estricto, Grafo Neural Tridimensional en WebGL, Neuroplasticidad en Tiempo Real y Cero Fuga de Datos (Air-Gapped Ready).">
  <meta name="author" content="AS - MAPPS Brasil: Leandro Bruzzese, Gustavo Costa Berbert, Marcio Miguel">
  <link rel="icon" type="image/png" href="assets/logo_stacked.png">
  <link rel="apple-touch-icon" href="assets/logo_stacked.png">

  <!-- Open Graph / Rich Social Preview (Teams, WhatsApp, Slack, LinkedIn) -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://gberbert.github.io/mapps_br_neuralgraph/">
  <meta property="og:title" content="AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA">
  <meta property="og:description" content="Presentación Ejecutiva de la Plataforma AXET-NeuralGraph 3D para MAPFRE Seguros. RAG Local-First Estricto, Grafo 3D WebGL a 60 FPS y Cero Fuga de Datos.">
  <meta property="og:image" content="https://gberbert.github.io/mapps_br_neuralgraph/assets/og_preview.png">
  <meta property="og:image:secure_url" content="https://gberbert.github.io/mapps_br_neuralgraph/assets/og_preview.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="NTT DATA & MAPFRE — AXET-NeuralGraph 3D">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA">
  <meta name="twitter:description" content="Presentación Ejecutiva de la Plataforma AXET-NeuralGraph 3D para MAPFRE Seguros.">
  <meta name="twitter:image" content="https://gberbert.github.io/mapps_br_neuralgraph/assets/og_preview.png">
  <link rel="image_src" href="https://gberbert.github.io/mapps_br_neuralgraph/assets/og_square.png">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- Chart.js via CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <style>
    :root {{
      /* Dark Theme (Default) */
      --bg-primary: #070a13;
      --bg-surface: #0d1322;
      --bg-card: rgba(15, 23, 42, 0.82);
      --bg-card-hover: rgba(22, 34, 61, 0.92);
      --bg-glass: rgba(255, 255, 255, 0.04);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-highlight: rgba(0, 102, 255, 0.45);
      --border-subtle: rgba(255, 255, 255, 0.04);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      /* Brand Identity Colors */
      --ntt-blue: #0066ff;
      --ntt-blue-light: #38bdf8;
      --ntt-cyan: #00c0f3;
      --mapfre-red: #d31027;
      --mapfre-red-glow: rgba(211, 16, 39, 0.35);
      
      --success: #10b981;
      --warning: #f59e0b;
      --danger: #ef4444;
      --purple: #8b5cf6;
      
      --shadow-lg: 0 20px 35px -10px rgba(0, 0, 0, 0.65), 0 8px 12px -6px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 25px rgba(0, 102, 255, 0.28);
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    body[data-theme="light"] {{
      --bg-primary: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.95);
      --bg-card-hover: rgba(241, 245, 249, 0.98);
      --bg-glass: rgba(0, 0, 0, 0.03);
      --border-color: rgba(0, 0, 0, 0.1);
      --border-highlight: rgba(0, 102, 255, 0.5);
      --border-subtle: rgba(0, 0, 0, 0.05);
      
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #64748b;
      
      --shadow-lg: 0 20px 30px -10px rgba(0, 0, 0, 0.1), 0 8px 12px -6px rgba(0, 0, 0, 0.06);
      --shadow-glow: 0 0 25px rgba(0, 102, 255, 0.15);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      transition: background-color 0.4s ease, color 0.4s ease;
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(0, 102, 255, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 85%, rgba(0, 192, 243, 0.09) 0%, transparent 45%);
      background-attachment: fixed;
    }}

    /* ── TOPBAR NAVIGATION ────────────────────────────────────────────── */
    .topbar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 68px;
      background: var(--bg-surface);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.75rem;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
      white-space: nowrap;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 1.15rem;
      flex-shrink: 0;
    }}

    .brand-logos-capsule {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      background: #ffffff;
      padding: 4px 10px;
      border-radius: 10px;
      border: 1px solid rgba(0, 0, 0, 0.12);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.18);
      flex-shrink: 0;
      height: 48px;
    }}

    .brand-logo-img {{
      height: 16px;
      width: auto;
      max-width: 85px;
      object-fit: contain;
      display: block;
    }}

    .brand-logo-sep {{
      width: 44px;
      height: 1px;
      background: #cbd5e1;
    }}

    .brand-title-block {{
      display: flex;
      flex-direction: column;
      justify-content: center;
      line-height: 1.25;
      flex-shrink: 0;
    }}

    .brand-title-row {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      white-space: nowrap;
    }}

    .brand-name {{
      background: linear-gradient(135deg, #ffffff 40%, var(--ntt-blue-light) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    body[data-theme="light"] .brand-name {{
      background: linear-gradient(135deg, #0f172a 40%, var(--ntt-blue) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .brand-tag {{
      color: var(--ntt-cyan);
      font-size: 0.85rem;
      font-weight: 600;
    }}

    .brand-subtitle {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 400;
      white-space: nowrap;
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 0.55rem;
      flex-shrink: 0;
      white-space: nowrap;
    }}

    /* Language Switcher */
    .lang-switcher {{
      display: flex;
      align-items: center;
      background: var(--bg-glass);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 2px;
      gap: 2px;
      flex-shrink: 0;
    }}

    .lang-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-family: 'Outfit', sans-serif;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 5px 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: var(--transition);
      line-height: 1;
    }}

    .lang-btn:hover {{
      color: var(--text-main);
    }}

    .lang-btn.active {{
      background: var(--ntt-blue);
      color: #ffffff;
      box-shadow: 0 1px 6px rgba(0, 102, 255, 0.4);
    }}

    /* Progress Bar */
    .progress-bar-container {{
      position: fixed;
      top: 68px;
      left: 0;
      right: 0;
      height: 4px;
      background: rgba(255, 255, 255, 0.05);
      z-index: 999;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--ntt-blue), var(--ntt-cyan));
      width: 10%;
      transition: width 0.35s ease;
      box-shadow: 0 0 10px var(--ntt-cyan);
    }}

    /* Nav Buttons */
    .btn-nav {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.45rem 0.85rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: var(--transition);
      user-select: none;
      white-space: nowrap;
      flex-shrink: 0;
    }}

    .btn-nav:hover:not(:disabled) {{
      background: var(--bg-card-hover);
      border-color: var(--border-highlight);
      box-shadow: var(--shadow-glow);
      transform: translateY(-1px);
    }}

    .btn-nav:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
      filter: grayscale(1);
    }}

    .slide-counter {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      padding: 0.4rem 0.75rem;
      background: rgba(0, 192, 243, 0.08);
      border: 1px solid rgba(0, 192, 243, 0.25);
      border-radius: 8px;
      min-width: 78px;
      text-align: center;
      flex-shrink: 0;
    }}

    /* Main Slides Container */
    main.presentation-wrapper {{
      flex: 1;
      margin-top: 72px;
      display: flex;
      flex-direction: column;
      position: relative;
    }}

    .slide-container {{
      display: none;
      min-height: calc(100vh - 72px);
      padding: 2.25rem 3.5rem 5rem 3.5rem;
      opacity: 0;
      transform: scale(0.99) translateY(8px);
      transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .slide-container.active {{
      display: flex;
      flex-direction: column;
      opacity: 1;
      transform: scale(1) translateY(0);
    }}

    /* Typography & Headers */
    .slide-header {{
      margin-bottom: 1.75rem;
    }}

    .slide-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--ntt-cyan);
      background: rgba(0, 192, 243, 0.12);
      border: 1px solid rgba(0, 192, 243, 0.3);
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.75rem;
    }}

    .slide-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.2;
      color: var(--text-main);
      margin-bottom: 0.5rem;
    }}

    .slide-title span.accent {{
      background: linear-gradient(135deg, var(--ntt-blue-light) 0%, var(--ntt-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .slide-subtitle {{
      font-size: 1.02rem;
      color: var(--text-muted);
      line-height: 1.5;
      max-width: 1100px;
    }}

    /* Cards and Grids */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.5rem;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.35rem;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.15rem;
    }}

    .grid-6 {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 1rem;
    }}

    .card {{
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.4rem;
      box-shadow: var(--shadow-lg);
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}

    .card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, rgba(0, 102, 255, 0.5), transparent);
      opacity: 0;
      transition: var(--transition);
    }}

    .card:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-2px);
      box-shadow: var(--shadow-glow), var(--shadow-lg);
    }}

    .card:hover::before {{
      opacity: 1;
    }}

    .card-icon {{
      font-size: 1.6rem;
      margin-bottom: 0.75rem;
      width: 42px;
      height: 42px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      background: rgba(0, 102, 255, 0.12);
      border: 1px solid rgba(0, 102, 255, 0.25);
      color: var(--ntt-blue-light);
    }}

    .card-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.6rem;
      line-height: 1.3;
    }}

    .card-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    .highlight-pill {{
      margin-top: auto;
      padding-top: 0.85rem;
      font-size: 0.78rem;
      line-height: 1.45;
      color: var(--ntt-cyan);
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      display: flex;
      align-items: flex-start;
      gap: 0.4rem;
    }}

    /* Metrics & Stats */
    .stat-badge {{
      display: flex;
      flex-direction: column;
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.1rem;
      text-align: center;
      transition: var(--transition);
    }}
    .stat-badge:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-2px);
    }}
    .stat-number {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.1rem;
      font-weight: 800;
      background: linear-gradient(135deg, #ffffff, var(--ntt-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      line-height: 1.1;
    }}
    body[data-theme="light"] .stat-number {{
      background: linear-gradient(135deg, var(--ntt-blue), var(--ntt-cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .stat-label {{
      font-size: 0.76rem;
      color: var(--text-muted);
      margin-top: 0.35rem;
      font-weight: 500;
    }}

    /* Comparative Table (Slide 2) */
    .compare-table-wrap {{
      width: 100%;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      box-shadow: var(--shadow-lg);
    }}

    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }}

    .compare-table th {{
      background: rgba(0, 102, 255, 0.1);
      padding: 0.85rem 1.25rem;
      font-family: 'Outfit', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      border-bottom: 2px solid var(--border-highlight);
    }}

    .compare-table td {{
      padding: 0.75rem 1.25rem;
      font-size: 0.84rem;
      line-height: 1.5;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }}

    .compare-table tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    .col-dim {{
      font-weight: 700;
      color: var(--ntt-blue-light);
      width: 20%;
    }}

    .col-bad {{
      color: #fca5a5;
      width: 40%;
      background: rgba(239, 68, 68, 0.03);
    }}

    .col-good {{
      color: #86efac;
      width: 40%;
      background: rgba(16, 185, 129, 0.04);
      border-left: 1px solid rgba(16, 185, 129, 0.15);
    }}

    /* Interactive Simulation Box (Slide 6) */
    .sim-box {{
      background: #050811;
      border: 1px solid var(--border-highlight);
      border-radius: 14px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
    }}

    .sim-row {{
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      padding: 0.85rem 1rem;
      border-radius: 8px;
    }}

    .sim-row.user {{
      background: rgba(255, 255, 255, 0.03);
      border-left: 3px solid #94a3b8;
    }}

    .sim-row.bot {{
      background: rgba(0, 102, 255, 0.08);
      border-left: 3px solid var(--ntt-cyan);
    }}

    .sim-row.mutation {{
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.4);
    }}

    .sim-tag {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      text-transform: uppercase;
    }}

    .sim-text {{
      font-size: 0.88rem;
      line-height: 1.5;
      color: #f8fafc;
    }}

    /* Gallery Grid for Slide 8 */
    .gallery-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.25rem;
    }}

    .gallery-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      overflow: hidden;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
    }}

    .gallery-card:hover {{
      border-color: var(--ntt-cyan);
      transform: translateY(-3px);
      box-shadow: 0 10px 25px rgba(0, 192, 243, 0.2);
    }}

    .gallery-thumb-wrap {{
      width: 100%;
      height: 170px;
      overflow: hidden;
      position: relative;
      background: #000;
    }}

    .gallery-thumb-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }}

    .gallery-card:hover .gallery-thumb-wrap img {{
      transform: scale(1.05);
    }}

    .gallery-info {{
      padding: 1rem 1.15rem;
    }}

    .gallery-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 0.98rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.35rem;
    }}

    .gallery-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Image Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(8px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 2rem;
    }}

    .modal-overlay.open {{
      display: flex;
    }}

    .modal-content {{
      max-width: 90vw;
      max-height: 88vh;
      display: flex;
      flex-direction: column;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 25px 50px rgba(0,0,0,0.8);
      position: relative;
    }}

    .modal-content img {{
      max-width: 100%;
      max-height: 76vh;
      object-fit: contain;
    }}

    .modal-footer {{
      padding: 1rem 1.5rem;
      background: var(--bg-card);
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .modal-close-btn {{
      background: var(--mapfre-red);
      color: #fff;
      border: none;
      padding: 6px 16px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
    }}

    /* Presenter Notes Drawer */
    .presenter-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--bg-surface);
      border-top: 2px solid var(--border-highlight);
      box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.4);
      z-index: 990;
      transform: translateY(calc(100% - 36px));
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    .presenter-bar.open {{
      transform: translateY(0);
    }}

    .presenter-header {{
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      background: rgba(0, 102, 255, 0.08);
      cursor: pointer;
      user-select: none;
    }}

    .presenter-title {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .presenter-content {{
      padding: 1.25rem 2rem;
      max-height: 220px;
      overflow-y: auto;
      font-size: 0.95rem;
      line-height: 1.7;
      color: var(--text-main);
    }}

    /* Slide Drawer Modal */
    .slide-drawer-modal {{
      position: fixed;
      top: 68px;
      right: 0;
      bottom: 0;
      width: 360px;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-color);
      box-shadow: -15px 0 35px rgba(0, 0, 0, 0.5);
      z-index: 1050;
      transform: translateX(100%);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }}

    .slide-drawer-modal.open {{
      transform: translateX(0);
    }}

    .drawer-header {{
      padding: 1.25rem 1.5rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .drawer-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .drawer-close {{
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.4rem;
      cursor: pointer;
      padding: 0.2rem;
      line-height: 1;
    }}

    .drawer-list {{
      flex: 1;
      overflow-y: auto;
      padding: 1rem 0;
    }}

    .drawer-item {{
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.85rem;
      cursor: pointer;
      transition: var(--transition);
      border-left: 3px solid transparent;
    }}

    .drawer-item:hover {{
      background: var(--bg-glass);
      border-left-color: var(--ntt-cyan);
    }}

    .drawer-item.active {{
      background: rgba(0, 102, 255, 0.12);
      border-left-color: var(--ntt-blue);
    }}

    .drawer-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--ntt-cyan);
      min-width: 24px;
    }}

    .drawer-label {{
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--text-main);
    }}

    /* Leadership Signature Card */
    .leadership-card {{
      background: linear-gradient(135deg, rgba(0, 102, 255, 0.08) 0%, rgba(211, 16, 39, 0.05) 100%);
      border: 1px solid rgba(0, 102, 255, 0.3);
      border-radius: 16px;
      padding: 1.75rem 2rem;
      margin-top: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      position: relative;
    }}

    .leadership-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 0.85rem;
    }}

    .leadership-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--text-main);
    }}

    .leadership-subtitle {{
      font-size: 0.85rem;
      color: var(--ntt-cyan);
      font-weight: 600;
    }}

    .leadership-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.25rem;
    }}

    .leader-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.1rem;
      text-align: center;
    }}

    .leader-name {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.25rem;
    }}

    .leader-role {{
      font-size: 0.8rem;
      color: var(--ntt-blue-light);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    /* Charts Container */
    .chart-container-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.25rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      height: 310px;
      display: flex;
      flex-direction: column;
    }}

    .chart-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .chart-canvas-wrap {{
      flex: 1;
      position: relative;
      width: 100%;
      height: 100%;
    }}

    .stat-calc-chip {{
      margin-top: 6px;
      font-size: 0.68rem;
      font-weight: 700;
      color: #7dd3fc;
      background: rgba(14, 165, 233, 0.1);
      border: 1px solid rgba(14, 165, 233, 0.25);
      padding: 3px 8px;
      border-radius: 6px;
      display: inline-block;
      transition: all 0.2s;
    }}
    .stat-badge:hover .stat-calc-chip {{
      background: rgba(14, 165, 233, 0.2);
      border-color: rgba(14, 165, 233, 0.4);
      color: #38bdf8;
    }}

    /* Modal de Memoria de Cálculo */
    .calc-modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(10px);
      z-index: 2100;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}
    .calc-modal-overlay.open {{
      display: flex;
    }}
    .calc-modal-container {{
      width: 100%;
      max-width: 900px;
      max-height: 90vh;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0,0,0,0.85);
      animation: modalFadeIn 0.25s ease-out;
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .calc-modal-header {{
      padding: 1.25rem 1.75rem;
      background: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }}
    .calc-modal-tabs {{
      display: flex;
      background: rgba(0,0,0,0.25);
      border-bottom: 1px solid var(--border-color);
      padding: 0 1.5rem;
      overflow-x: auto;
      gap: 0.5rem;
    }}
    .calc-tab-btn {{
      padding: 0.85rem 1.1rem;
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--text-muted);
      border: none;
      background: none;
      cursor: pointer;
      border-bottom: 2px solid transparent;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .calc-tab-btn.active {{
      color: #38bdf8;
      border-bottom-color: #38bdf8;
    }}
    .calc-modal-body {{
      padding: 1.75rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .calc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.25rem;
    }}
    .calc-box-title {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--text-main);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .calc-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .calc-col {{
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      padding: 0.85rem 1rem;
      border-radius: 8px;
    }}
    .calc-col-label {{
      font-size: 0.72rem;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 0.35rem;
    }}
    .calc-col-val {{
      font-size: 0.85rem;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .calc-formula-banner {{
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 0.85rem 1.15rem;
      border-radius: 8px;
      font-family: monospace;
      font-size: 0.88rem;
      color: #6ee7b7;
      margin-bottom: 1rem;
    }}
    .calc-impact-box {{
      background: rgba(99, 102, 241, 0.08);
      border: 1px solid rgba(99, 102, 241, 0.25);
      padding: 0.85rem 1.15rem;
      border-radius: 8px;
      font-size: 0.84rem;
      color: #c7d2fe;
      line-height: 1.45;
    }}

    /* Responsive Rules */
    @media (max-width: 1250px) {{
      .brand-subtitle {{
        display: none;
      }}
    }}
    @media (max-width: 900px) {{
      .topbar {{
        padding: 0 1rem;
      }}
      .brand-logos-capsule {{
        display: none;
      }}
      .slide-container {{
        padding: 1.5rem 1.5rem 5rem 1.5rem;
      }}
      .grid-3, .grid-4, .grid-6, .gallery-grid, .leadership-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Topbar -->
  <header class="topbar">
    <div class="brand-group">
      <!-- Official Logos Capsule: NTT DATA on top, MAPFRE on bottom -->
      <div class="brand-logos-capsule" title="NTT DATA & MAPFRE">
        <img class="brand-logo-img" src="{b64_ntt}" alt="NTT DATA" onerror="this.src='assets/logo_nttdata.png'">
        <div class="brand-logo-sep"></div>
        <img class="brand-logo-img" src="{b64_mapfre}" alt="MAPFRE" onerror="this.src='assets/logo_mapfre.png'">
      </div>

      <div class="brand-title-block">
        <div class="brand-title-row">
          <span class="brand-name">AXET-NeuralGraph 3D</span>
          <span class="brand-tag">| <span data-i18n="topbar_title_tag">Plataforma Cognitiva Desktop</span></span>
        </div>
        <span class="brand-subtitle" data-i18n="topbar_subtitle">RAG Local-First Estricto • Grafo 3D • Cero Fuga de Datos (Air-Gapped)</span>
      </div>
    </div>

    <div class="nav-actions">
      <!-- Language Switcher: ES (Default), EN, PTB -->
      <div class="lang-switcher" role="group" aria-label="Selector de idioma">
        <button class="lang-btn active" data-lang="es" onclick="setLanguage('es')" title="Español (Predeterminado)">ES</button>
        <button class="lang-btn" data-lang="en" onclick="setLanguage('en')" title="English">EN</button>
        <button class="lang-btn" data-lang="ptb" onclick="setLanguage('ptb')" title="Português do Brasil">PTB</button>
      </div>

      <button class="btn-nav" id="btnPrev" title="Slide Anterior (Seta Esquerda)"><span data-i18n="nav_prev">◀ Anterior</span></button>
      <div class="slide-counter" id="slideNumDisplay">01 / 10</div>
      <button class="btn-nav" id="btnNext" title="Próximo Slide (Seta Direita / Barra de Espaço)"><span data-i18n="nav_next">Siguiente ▶</span></button>
      
      <button class="btn-nav" id="btnNotes" title="Notas do Apresentador (Tecla N)"><span data-i18n="btn_notes">Notas [N]</span></button>
      <button class="btn-nav" onclick="openCalcModal(1)" title="Memoria de Cálculo & Metodología" style="border-color: rgba(56, 189, 248, 0.4); background: rgba(56, 189, 248, 0.08);"><span data-i18n="s9_calc_btn">🧮 Memoria de Cálculo</span></button>
      <button class="btn-nav" id="btnDrawer" title="Índice de Slides"><span data-i18n="btn_drawer">Índice</span></button>
      <button class="btn-nav" id="btnTheme" title="Alternar Modo Escuro / Claro">🌓</button>
      <button class="btn-nav" id="btnFullscreen" title="Tela Cheia (Tecla F)">⛶</button>
    </div>
  </header>

  <!-- Progress Bar -->
  <div class="progress-bar-container">
    <div class="progress-fill" id="progress-fill"></div>
  </div>

  <!-- Main Presentation Slides -->
  <main class="presentation-wrapper">

    <!-- SLIDE 1: PORTADA EJECUTIVA -->
    <section class="slide-container active" data-slide="1">
      <div class="slide-header" style="max-width: 1200px;">
        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.85rem;">
          <span class="slide-tag" data-i18n="s1_badge1">PRODUCTO DESKTOP NATIVO</span>
          <span class="slide-tag" style="color: var(--success); background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.3);" data-i18n="s1_badge2">AIR-GAPPED 100% LOCALHOST</span>
          <span class="slide-tag" style="color: var(--purple); background: rgba(139, 92, 246, 0.12); border-color: rgba(139, 92, 246, 0.3);" data-i18n="s1_badge3">THREE.JS WEBGL 60FPS</span>
          <span class="slide-tag" style="color: var(--ntt-blue-light); background: rgba(0, 102, 255, 0.12); border-color: rgba(0, 102, 255, 0.3);" data-i18n="s1_badge4">TAURI V2 RUST</span>
          <span class="slide-tag" style="color: var(--warning); background: rgba(245, 158, 11, 0.12); border-color: rgba(245, 158, 11, 0.3);" data-i18n="s1_badge5">INTEGRIDAD SHA-256</span>
        </div>
        <h1 class="slide-title" style="font-size: 2.9rem; line-height: 1.15;">
          <span class="accent" data-i18n="s1_title">AXET-NeuralGraph 3D</span><br>
          <span style="font-size: 1.65rem; font-weight: 600; color: var(--text-main);" data-i18n="s1_title_accent">Plataforma Cognitiva Desktop para Reglas Técnicas & Acervos de Misión Crítica (Reef.core)</span>
        </h1>
        <p class="slide-subtitle" style="font-size: 1.05rem; margin-top: 1rem;" data-i18n="s1_lead">
          Ecosistema corporativo de inteligencia artificial soberana concebido por <strong>NTT DATA</strong> para <strong>MAPFRE</strong>...
        </p>
      </div>

      <!-- 6 Key Metrics -->
      <div class="grid-6" style="margin-top: 1.5rem;">
        <div class="stat-badge">
          <div class="stat-number" data-i18n="s1_stat1_num">3.111+</div>
          <div class="stat-label" data-i18n="s1_stat1_lbl">Nodos en Malla Encefálica</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" data-i18n="s1_stat2_num">9.472+</div>
          <div class="stat-label" data-i18n="s1_stat2_lbl">Sinapsis & Aristas Relacionales</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" data-i18n="s1_stat3_num">&lt; 100 MB</div>
          <div class="stat-label" data-i18n="s1_stat3_lbl">Consumo RAM (Tauri v2 Rust)</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" data-i18n="s1_stat4_num">100%</div>
          <div class="stat-label" data-i18n="s1_stat4_lbl">Localhost Air-Gapped (Cero Nube)</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--ntt-cyan);" data-i18n="s1_stat5_num">+1.000 h</div>
          <div class="stat-label" data-i18n="s1_stat5_lbl">Video Técnico Indexado</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--success);" data-i18n="s1_stat6_num">+2.000</div>
          <div class="stat-label" data-i18n="s1_stat6_lbl">Docs Técnicos Reef.core</div>
        </div>
      </div>

      <div style="margin-top: 1.75rem; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-size: 0.9rem; color: var(--text-dim); font-style: italic; max-width: 750px;" data-i18n="s1_quote">
          «La única solución para acervos actuariales hipercomplejos que garantiza soberanía absoluta, cero telemetría externa y rendimiento a 60 FPS.»
        </div>
        <button class="btn-nav" onclick="updateSlide(2)" style="background: var(--ntt-blue); color: #fff; padding: 0.75rem 1.5rem; font-size: 0.95rem; border-color: var(--ntt-blue); border-radius: 10px;">
          <span data-i18n="s1_cta">Explorar Arquitectura y Pilares ➔</span>
        </button>
      </div>
    </section>

    <!-- SLIDE 2: COMPARATIVA CRÍTICA: NUBE VS DESKTOP -->
    <section class="slide-container" data-slide="2">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s2_tag">Diagnóstico Crítico & Comparativa</span>
        <h2 class="slide-title" data-i18n="s2_title">¿Por Qué un Producto Desktop Nativo y No una Solución Web Cloud?</h2>
        <p class="slide-subtitle" data-i18n="s2_subtitle">Matriz de decisión estratégica: cómo AXET neutralizó los riesgos de fuga de propiedad intelectual, latencia y envenenamiento de memoria.</p>
      </div>

      <div class="compare-table-wrap">
        <table class="compare-table">
          <thead>
            <tr>
              <th data-i18n="s2_table_h1">Dimensión Operacional</th>
              <th data-i18n="s2_table_h2">Solución Web Cloud (OpenAI / AWS)</th>
              <th data-i18n="s2_table_h3">AXET-NeuralGraph 3D Desktop</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="col-dim" data-i18n="s2_row1_dim">Soberanía y Fuga de Datos</td>
              <td class="col-bad" data-i18n="s2_row1_bad">❌ Reglas y fórmulas enviadas a APIs de terceros...</td>
              <td class="col-good" data-i18n="s2_row1_good">✅ 100% Localhost (127.0.0.1). Ni un byte sale de la máquina...</td>
            </tr>
            <tr>
              <td class="col-dim" data-i18n="s2_row2_dim">Cumplimiento Regulatorio</td>
              <td class="col-bad" data-i18n="s2_row2_bad">❌ Incumplimiento de normativas de custodia...</td>
              <td class="col-good" data-i18n="s2_row2_good">✅ Cumplimiento pleno Air-Gapped Ready...</td>
            </tr>
            <tr>
              <td class="col-dim" data-i18n="s2_row3_dim">Latencia & Conectividad</td>
              <td class="col-bad" data-i18n="s2_row3_bad">❌ Dependencia de enlaces externos (3-8s)...</td>
              <td class="col-good" data-i18n="s2_row3_good">✅ Procesamiento en RAM y GPU local (<500ms)...</td>
            </tr>
            <tr>
              <td class="col-dim" data-i18n="s2_row4_dim">Blindaje Epistémico</td>
              <td class="col-bad" data-i18n="s2_row4_bad">❌ Vulnerable a Data Poisoning...</td>
              <td class="col-good" data-i18n="s2_row4_good">✅ Blindaje Epistémico Estricto con anexos efímeros...</td>
            </tr>
            <tr>
              <td class="col-dim" data-i18n="s2_row5_dim">Coste Operacional (TCO)</td>
              <td class="col-bad" data-i18n="s2_row5_bad">❌ Facturación recurrente por token exponencial...</td>
              <td class="col-good" data-i18n="s2_row5_good">✅ Coste marginal cero: aprovecha hardware ya disponible...</td>
            </tr>
            <tr>
              <td class="col-dim" data-i18n="s2_row6_dim">Experiencia Visual</td>
              <td class="col-bad" data-i18n="s2_row6_bad">❌ Interfaces de chat planas sin visión relacional...</td>
              <td class="col-good" data-i18n="s2_row6_good">✅ Grafo Neural 3D inmersivo a 60 FPS con navegación anatómica...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SLIDE 3: LOS 6 PILARES TECNOLÓGICOS -->
    <section class="slide-container" data-slide="3">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s3_tag">Ecosistema Cognitivo</span>
        <h2 class="slide-title" data-i18n="s3_title">La Ventaja de AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos</h2>
        <p class="slide-subtitle" data-i18n="s3_subtitle">Una suite de ingeniería integral concebida para transformar documentación dispersa en un activo neural vivo y seguro.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-icon">🧠</div>
          <h3 class="card-title" data-i18n="s3_c1_title">1. Grafo Neural 3D Anatómico</h3>
          <p class="card-desc" data-i18n="s3_c1_desc">Malla encefálica tridimensional en WebGL (Three.js) con 3.111 nodos y 9.472 sinapsis distribuidos según la neuroanatomía humana real.</p>
          <div class="highlight-pill" data-i18n="s3_c1_pill">⚡ 3.111 nodos y 9.472 sinapsis con inspección 360°...</div>
        </div>

        <div class="card">
          <div class="card-icon">⚡</div>
          <h3 class="card-title" data-i18n="s3_c2_title">2. Neuroplasticidad en Tiempo Real</h3>
          <p class="card-desc" data-i18n="s3_c2_desc">Auto-rectificación sintética instantánea. Cuando se detecta un error de razonamiento, el sistema muta la memoria creando nodos de aprendizaje.</p>
          <div class="highlight-pill" data-i18n="s3_c2_pill">💡 Nó canónico APRENDIZADO_COGNITIVO (peso 2.5+)...</div>
        </div>

        <div class="card">
          <div class="card-icon">🌐</div>
          <h3 class="card-title" data-i18n="s3_c3_title">3. Federación Git Cero Permisos</h3>
          <p class="card-desc" data-i18n="s3_c3_desc">Colaboración distribuida sin credenciales de repositorio. Cientos de usuarios comparten sinapsis vía Outbox local e Issues etiquetadas.</p>
          <div class="highlight-pill" data-i18n="s3_c3_pill">🔒 Cero privilegios requeridos en el usuario final...</div>
        </div>

        <div class="card">
          <div class="card-icon">🛡️</div>
          <h3 class="card-title" data-i18n="s3_c4_title">4. RAG Local-First Estricto</h3>
          <p class="card-desc" data-i18n="s3_c4_desc">Aislamiento total en localhost (127.0.0.1). Entrega de conocimiento por snapshots cifrados (.qpack) con verificación SHA-256 y blindaje epistémico.</p>
          <div class="highlight-pill" data-i18n="s3_c4_pill">🛑 Prevención absoluta de Data Poisoning...</div>
        </div>

        <div class="card">
          <div class="card-icon">📎</div>
          <h3 class="card-title" data-i18n="s3_c5_title">5. Chat Multimodal con Telemetría SSE</h3>
          <p class="card-desc" data-i18n="s3_c5_desc">Lectura nativa en memoria de PDFs corporativos, PPTs y DOCX, con visión computacional y streaming de estado en tiempo real vía Server-Sent Events.</p>
          <div class="highlight-pill" data-i18n="s3_c5_pill">📊 Telemetría en tiempo real paso a paso...</div>
        </div>

        <div class="card">
          <div class="card-icon">⚖️</div>
          <h3 class="card-title" data-i18n="s3_c6_title">6. Matriz Regulatoria & Glosario De ➔ Para</h3>
          <p class="card-desc" data-i18n="s3_c6_desc">Módulo administrativo que armoniza órganos reguladores por país (SUSEP Brasil, DGSFP España) con thesaurus semántico para equivalencia inmediata.</p>
          <div class="highlight-pill" data-i18n="s3_c6_pill">🏛️ Adaptación instantánea de términos por jurisdicción...</div>
        </div>
      </div>
    </section>

    <!-- SLIDE 4: GRAFO 3D Y LÓBULOS CORTICALES -->
    <section class="slide-container" data-slide="4">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s4_tag">Cartografía Cognitiva</span>
        <h2 class="slide-title" data-i18n="s4_title">Grafo Neural 3D: Cartografía del Encéfalo de Misión Crítica</h2>
        <p class="slide-subtitle" data-i18n="s4_subtitle">Navegación espacial interactiva a 60 FPS estructurada según la especialización funcional de los lóbulos cerebrales.</p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1.25fr; gap: 1.5rem; align-items: start;">
        <!-- Left: 5 Lobes Detailed Cards -->
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          <div class="card" style="padding: 0.95rem; border-left: 4px solid var(--ntt-blue);">
            <h4 class="card-title" style="font-size: 0.95rem; margin-bottom: 0.25rem;" data-i18n="s4_l1_title">Lóbulo Temporal (36% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.82rem;" data-i18n="s4_l1_desc">Memoria declarativa y semántica profunda. Alberga pólizas maestras, contratos y Reef.core.</p>
          </div>
          <div class="card" style="padding: 0.95rem; border-left: 4px solid var(--ntt-cyan);">
            <h4 class="card-title" style="font-size: 0.95rem; margin-bottom: 0.25rem;" data-i18n="s4_l2_title">Lóbulo Frontal (28% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.82rem;" data-i18n="s4_l2_desc">Corteza prefrontal ejecutiva. Orquesta la toma de decisiones, reglas DUP y tarificación.</p>
          </div>
          <div class="card" style="padding: 0.95rem; border-left: 4px solid var(--purple);">
            <h4 class="card-title" style="font-size: 0.95rem; margin-bottom: 0.25rem;" data-i18n="s4_l3_title">Lóbulo Parietal (24% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.82rem;" data-i18n="s4_l3_desc">Integración técnica y conectividad. Endpoints de API, esquemas JSON y microservicios.</p>
          </div>
          <div class="card" style="padding: 0.95rem; border-left: 4px solid var(--warning);">
            <h4 class="card-title" style="font-size: 0.95rem; margin-bottom: 0.25rem;" data-i18n="s4_l4_title">Lóbulo Occipital (8% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.82rem;" data-i18n="s4_l4_desc">Procesamiento multimodal visual. Diagramas de arquitectura y pantallas de sistemas.</p>
          </div>
          <div class="card" style="padding: 0.95rem; border-left: 4px solid var(--success);">
            <h4 class="card-title" style="font-size: 0.95rem; margin-bottom: 0.25rem;" data-i18n="s4_l5_title">Cerebelo & Tronco Encefálico (4%)</h4>
            <p class="card-desc" style="font-size: 0.82rem;" data-i18n="s4_l5_desc">Control motor, ingestión continua y telemetría SSE a 60 FPS.</p>
          </div>
        </div>

        <!-- Right: Screen Preview + Technical Stack Box -->
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div class="card" style="padding: 0.5rem; overflow: hidden; cursor: pointer;" onclick="openImageModal('assets/screen_neural_graph_3d.jpg', 'Grafo Neural Tridimensional (Three.js WebGL)')">
            <img src="assets/screen_neural_graph_3d.jpg" alt="Grafo Neural 3D" style="width: 100%; height: 280px; object-fit: cover; border-radius: 10px; display: block;">
            <div style="padding: 0.6rem 0.8rem; font-size: 0.8rem; color: var(--ntt-cyan); font-weight: 600; text-align: center;">
              🔍 Clic para ampliar captura real en 4K (Renderizado WebGL nativo)
            </div>
          </div>

          <div class="card" style="background: rgba(0, 102, 255, 0.06); border-color: rgba(0, 102, 255, 0.3);">
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: var(--ntt-blue-light); font-weight: 700; margin-bottom: 0.35rem;">ESPECIFICACIÓN DE RENDERIZADO GRÁFICO:</div>
            <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;" data-i18n="s4_tech_spec">
              Tecnología: WebGL nativo a 60 FPS con Three.js, shaders espaciales personalizados, bloom post-processing, carga optimizada de brain.glb y raycasting para inspección 360° en tiempo real.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 5: RAG LOCAL-FIRST & BLINDAJE EPISTÉMICO -->
    <section class="slide-container" data-slide="5">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s5_tag">Soberanía & Seguridad</span>
        <h2 class="slide-title" data-i18n="s5_title">RAG Local-First Estricto & Blindaje Epistémico</h2>
        <p class="slide-subtitle" data-i18n="s5_subtitle">La garantía matemática de que el conocimiento sensible de MAPFRE nunca sale de la estación de trabajo y nunca es corrompido.</p>
      </div>

      <div class="grid-4" style="margin-top: 1rem;">
        <div class="card" style="border-top: 3px solid var(--success);">
          <div class="card-icon" style="color: var(--success); background: rgba(16, 185, 129, 0.12);">🔒</div>
          <h3 class="card-title" data-i18n="s5_p1_title">1. Inviolabilidad de Localhost</h3>
          <p class="card-desc" data-i18n="s5_p1_desc">Embeddings densos de 1536d y búsqueda vectorial en 127.0.0.1. Ni una sola consulta o fragmento de contrato viaja por internet.</p>
        </div>

        <div class="card" style="border-top: 3px solid var(--ntt-cyan);">
          <div class="card-icon" style="color: var(--ntt-cyan); background: rgba(0, 192, 243, 0.12);">📦</div>
          <h3 class="card-title" data-i18n="s5_p2_title">2. Snapshots .qpack SHA-256</h3>
          <p class="card-desc" data-i18n="s5_p2_desc">Distribución en paquetes binarios cifrados (.qpack). El motor valida criptográficamente el hash SHA-256 al iniciar el sistema.</p>
        </div>

        <div class="card" style="border-top: 3px solid var(--purple);">
          <div class="card-icon" style="color: var(--purple); background: rgba(139, 92, 246, 0.12);">🛡️</div>
          <h3 class="card-title" data-i18n="s5_p3_title">3. Blindaje Epistémico</h3>
          <p class="card-desc" data-i18n="s5_p3_desc">Los adjuntos en el chat viven solo en RAM efímera: <strong>tienen prohibido persistirse o crear sinapsis</strong>, eliminando el Data Poisoning.</p>
        </div>

        <div class="card" style="border-top: 3px solid var(--warning);">
          <div class="card-icon" style="color: var(--warning); background: rgba(245, 158, 11, 0.12);">✈️</div>
          <h3 class="card-title" data-i18n="s5_p4_title">4. Air-Gapped Ready</h3>
          <p class="card-desc" data-i18n="s5_p4_desc">Preparado para salas de máxima seguridad sin conexión a redes externas, garantizando continuidad en caídas de telecomunicaciones.</p>
        </div>
      </div>

      <!-- Security Callout Banner -->
      <div class="card" style="margin-top: 1.25rem; background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.25); display: flex; flex-direction: row; align-items: center; justify-content: space-between; padding: 1rem 1.75rem;">
        <div style="display: flex; align-items: center; gap: 1rem;">
          <div style="font-size: 2rem;">🛡️</div>
          <div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 1rem; font-weight: 700; color: var(--text-main);">GARANTÍA CRIPTOGRÁFICA DE SOBERANÍA DOCUMENTAL</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;">SHA-256: <code>e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</code> • Cero archivos planos en disco</div>
          </div>
        </div>
        <span class="slide-tag" style="margin: 0; color: var(--success); border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.1);">COMPLIANCE SUSEP & DGSFP</span>
      </div>
    </section>

    <!-- SLIDE 6: NEUROPLASTICIDAD & MUTACIÓN EN CALIENTE -->
    <section class="slide-container" data-slide="6">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s6_tag">IA con Aprendizaje Continuo</span>
        <h2 class="slide-title" data-i18n="s6_title">Neuroplasticidad Sintética: Auto-Rectificación en Tiempo Real</h2>
        <p class="slide-subtitle" data-i18n="s6_subtitle">El agente que detecta fallos en su propio razonamiento y muta su topología de conocimiento de forma instantánea y verificable.</p>
      </div>

      <div style="display: grid; grid-template-columns: 1.25fr 1fr; gap: 1.5rem; align-items: start;">
        <!-- Left: Interactive Simulation Dialogue -->
        <div class="sim-box">
          <div class="sim-row user">
            <span class="sim-tag" data-i18n="s6_chat_q_title">CONSULTA DEL ACTUARIO (MAPFRE SEGUROS):</span>
            <p class="sim-text" data-i18n="s6_chat_q_text">«¿La regla de carencia G2002151 en el ramo Autos sigue aplicando el factor de 30 días para contratos emitidos a partir de enero de 2026?»</p>
          </div>

          <div class="sim-row bot">
            <span class="sim-tag" data-i18n="s6_chat_a_title">AUTO-RECTIFICACIÓN DEL COPILOT (TELEMETRÍA 480ms):</span>
            <p class="sim-text" data-i18n="s6_chat_a_text">«Divergencia detectada entre manual legado (30 días) y la Circular Normativa SUSEP N° 682 (15 días). Aplicando corrección canónica: la carencia fue reducida a 15 días corridos.»</p>
          </div>

          <div class="sim-row mutation">
            <span class="sim-tag" style="color: var(--success);" data-i18n="s6_chat_mut_title">MUTAÇÃO NEURAL OCORRIDA:</span>
            <p class="sim-text" style="color: #a7f3d0;" data-i18n="s6_chat_mut_text">⚡ Nuevo nodo canónico creado: APRENDIZADO_COGNITIVO[G2002151_2026] vinculado con arista RETIFICA_CONCEITO (peso reforzado: 2.85x).</p>
          </div>
        </div>

        <!-- Right: 3 Phases of Convergence -->
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div class="card" style="border-left: 4px solid var(--ntt-blue); padding: 1.1rem;">
            <h4 class="card-title" style="font-size: 1rem; margin-bottom: 0.35rem;" data-i18n="s6_step1_title">FASE 1: Detección de Inconsistencia</h4>
            <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s6_step1_desc">El motor contrasta la formulación generada contra las reglas consolidadas y las observaciones del especialista, identificando desfases normativos.</p>
          </div>

          <div class="card" style="border-left: 4px solid var(--ntt-cyan); padding: 1.1rem;">
            <h4 class="card-title" style="font-size: 1rem; margin-bottom: 0.35rem;" data-i18n="s6_step2_title">FASE 2: Mutación Topológica Inmediata</h4>
            <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s6_step2_desc">El grafo y la memoria vectorial mutan en caliente, registrando el aprendizaje con metadatos de autoría, fecha y justificación técnica.</p>
          </div>

          <div class="card" style="border-left: 4px solid var(--success); padding: 1.1rem;">
            <h4 class="card-title" style="font-size: 1rem; margin-bottom: 0.35rem;" data-i18n="s6_step3_title">FASE 3: Prevalencia Canónica Universal</h4>
            <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s6_step3_desc">Cualquier consulta subsiguiente de cualquier usuario de la compañía prioriza de inmediato el nodo rectificado sobre la documentación histórica desactualizada.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 7: FEDERACIÓN GIT CERO PERMISOS -->
    <section class="slide-container" data-slide="7">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s7_tag">Gobernanza Distribuida</span>
        <h2 class="slide-title" data-i18n="s7_title">Federación Git Cero Permisos: Colaboración a Escala</h2>
        <p class="slide-subtitle" data-i18n="s7_subtitle">Cientos de colaboradores sincronizando mejoras de conocimiento sin requerir credenciales ni permisos de commit en el código.</p>
      </div>

      <div class="grid-4" style="margin-top: 1rem;">
        <div class="card">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.3rem; font-weight: 800; color: var(--ntt-blue-light); margin-bottom: 0.5rem;" data-i18n="s7_flow1_num">01</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_flow1_title">Outbox Local Desacoplado</h3>
          <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s7_flow1_desc">Cada aprendizaje generado por el especialista se serializa en la bandeja de salida local de su estación de trabajo, sin requerir login ni tokens de desarrollador en GitHub.</p>
        </div>

        <div class="card">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.3rem; font-weight: 800; color: var(--ntt-cyan); margin-bottom: 0.5rem;" data-i18n="s7_flow2_num">02</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_flow2_title">Canal de Issues Etiquetadas</h3>
          <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s7_flow2_desc">El cliente desktop transmite los paquetes de sinapsis como GitHub Issues con el rótulo 'cognitive-learning', manteniendo el código fuente y las ramas principales 100% blindadas.</p>
        </div>

        <div class="card">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.3rem; font-weight: 800; color: var(--purple); margin-bottom: 0.5rem;" data-i18n="s7_flow3_num">03</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_flow3_title">Curaduría del Master Admin</h3>
          <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s7_flow3_desc">En la consola web de administración, los líderes técnicos de MAPFRE auditan las propuestas con análisis visual de impacto en el grafo antes de aprobar la incorporación oficial.</p>
        </div>

        <div class="card">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.3rem; font-weight: 800; color: var(--success); margin-bottom: 0.5rem;" data-i18n="s7_flow4_num">04</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_flow4_title">Release Global en &lt; 2s</h3>
          <p class="card-desc" style="font-size: 0.84rem;" data-i18n="s7_flow4_desc">El pipeline compila el nuevo paquete binario consolidado (.pack) y lo despliega mediante GitHub Releases. Todos los clientes desktop se sincronizan en segundo plano en instantes.</p>
        </div>
      </div>

      <!-- Security Guarantee Box -->
      <div class="card" style="margin-top: 1.25rem; background: rgba(0, 102, 255, 0.05); border: 1px solid rgba(0, 102, 255, 0.25); padding: 1rem 1.5rem;">
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <div style="font-size: 0.88rem; color: var(--text-main);">
            🔒 <strong>Blindaje Absoluto de Infraestructura:</strong> Los usuarios finales no poseen permisos de commit ni acceso a ramas protegidas. Ningún token sensible se expone en las máquinas cliente.
          </div>
          <span class="slide-tag" style="margin: 0; color: var(--ntt-cyan);">ZERO TRUST REPO</span>
        </div>
      </div>
    </section>

    <!-- SLIDE 8: GALERÍA DE PANTALLAS -->
    <section class="slide-container" data-slide="8">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s8_tag">Recorrido Visual del Producto</span>
        <h2 class="slide-title" data-i18n="s8_title">Galería de Pantallas Reales de la Aplicación Desktop</h2>
        <p class="slide-subtitle" data-i18n="s8_subtitle">Descubre cada módulo de la suite nativa de alto rendimiento desarrollada en Tauri v2, Next.js y Three.js.</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-card" onclick="openImageModal('assets/screen_neural_graph_3d.jpg', 'Grafo Neural 3D en WebGL')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_neural_graph_3d.jpg" alt="Grafo 3D">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m1_title">Grafo Neural 3D en WebGL</h4>
            <p class="gallery-desc" data-i18n="s8_m1_desc">Malla encefálica interactiva navegable con 3.111 nodos corticales mapeados espacialmente con shader bloom.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_node_inspection.jpg', 'Inspección de Nodos Semánticos')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_node_inspection.jpg" alt="Inspección de Nodos">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m2_title">Inspección de Nodos Semánticos</h4>
            <p class="gallery-desc" data-i18n="s8_m2_desc">Detalle técnico profundo con sinapsis activas, procedencia documental y autoridad de Reef Academy.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_graph_immersive.jpg', 'Asistente Cognitivo Inmersivo')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_graph_immersive.jpg" alt="Asistente Inmersivo">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m3_title">Asistente Cognitivo Inmersivo</h4>
            <p class="gallery-desc" data-i18n="s8_m3_desc">Copilot integrado directamente en el universo neural 3D recapitulando diálogos anteriores y contexto.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_chat_streaming.jpg', 'Chat con Streaming SSE')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_chat_streaming.jpg" alt="Chat SSE">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m4_title">Chat con Streaming SSE</h4>
            <p class="gallery-desc" data-i18n="s8_m4_desc">Telemetría dinámica paso a paso, carga nativa de PDFs/PPTs/Word y muestreo de imágenes Pillow a 1080p.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_home_dashboard.jpg', 'Dashboard Inicial')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_home_dashboard.jpg" alt="Dashboard">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m5_title">Dashboard con Okta SSO</h4>
            <p class="gallery-desc" data-i18n="s8_m5_desc">Punto de entrada con perfil corporativo unificado, estado del motor RAG local y preguntas sugeridas de negocio.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_admin_regulatory.jpg', 'Matriz Regulatoria')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_admin_regulatory.jpg" alt="Matriz Regulatoria">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_m6_title">Panel de Matriz Regulatoria</h4>
            <p class="gallery-desc" data-i18n="s8_m6_desc">Control administrativo de órganos reguladores (SUSEP / DGSFP) y glosario De ➔ Para con equivalencias automáticas.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 9: ARQUITECTURA EN 4 CAPAS Y BENCHMARKS -->
    <section class="slide-container" data-slide="9">
      <div class="slide-header" style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1rem;">
        <div>
          <span class="slide-tag" data-i18n="s9_tag">Ingeniería & Resultados</span>
          <h2 class="slide-title" data-i18n="s9_title">Arquitectura en 4 Capas & Benchmarks Mensurados</h2>
          <p class="slide-subtitle" data-i18n="s9_subtitle">Robustez técnica comprobada y retorno de inversión mensurado tras el despliegue del sistema.</p>
        </div>
        <button class="calc-btn" onclick="openCalcModal(1)">
          <span>🧮</span> <span data-i18n="s9_calc_btn">Ver Memoria de Cálculo & Metodología</span>
        </button>
      </div>

      <div class="grid-2">
        <!-- Left: 4-Layer Architecture Cards -->
        <div style="display: flex; flex-direction: column; gap: 0.75rem;">
          <div class="card" style="padding: 0.85rem 1rem; border-left: 4px solid var(--ntt-blue);">
            <div style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_layer1_name">Capa 1: Desktop Shell Nativo</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;" data-i18n="s9_layer1_desc">Tauri v2 (Rust) • Binario nativo (<100MB RAM) • macOS (.dmg) y Windows (.msi) • Seletor OneDrive.</div>
          </div>
          <div class="card" style="padding: 0.85rem 1rem; border-left: 4px solid var(--ntt-cyan);">
            <div style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_layer2_name">Capa 2: Frontend Reativo 60 FPS</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;" data-i18n="s9_layer2_desc">Next.js 14 + Three.js • WebGL 60 FPS con GLTFLoader • Shaders espaciales y Tailwind CSS.</div>
          </div>
          <div class="card" style="padding: 0.85rem 1rem; border-left: 4px solid var(--purple);">
            <div style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_layer3_name">Capa 3: Backend API Asíncrono</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;" data-i18n="s9_layer3_desc">FastAPI + Python 3.11 • Streaming de telemetría vía SSE • Validación Pydantic v2 • SQLAlchemy Asyncpg.</div>
          </div>
          <div class="card" style="padding: 0.85rem 1rem; border-left: 4px solid var(--success);">
            <div style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_layer4_name">Capa 4: Motores de IA & Persistencia</div>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.2rem;" data-i18n="s9_layer4_desc">Qdrant Vector DB (HNSW coseno) • Postgres 16 • Transcripción Faster-Whisper y FFmpeg.</div>
          </div>
        </div>

        <!-- Right: Charts -->
        <div style="display: flex; flex-direction: column; gap: 0.85rem;">
          <div class="chart-container-box" style="height: 180px;">
            <div class="chart-title">
              <span>⏱️</span> <span data-i18n="s9_chart1_title">Tiempo Medio de Resolución (Minutos)</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartResolutionTime"></canvas>
            </div>
          </div>

          <div class="chart-container-box" style="height: 180px;">
            <div class="chart-title">
              <span>🎯</span> <span data-i18n="s9_chart2_title">Evolución de Acuracia Cognitiva (%)</span>
            </div>
            <div class="chart-canvas-wrap">
              <canvas id="chartAccuracy"></canvas>
            </div>
          </div>
        </div>
      </div>

      <!-- Callout de Base Metodológica -->
      <div class="calc-callout" onclick="openCalcModal(1)">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
          <span style="font-size: 1.3rem;">📐</span>
          <div>
            <div style="font-weight: 700; font-size: 0.85rem; color: var(--ntt-cyan);" data-i18n="s9_calc_callout_title">BASE METODOLÓGICA Y MUESTREO AUDITADO (MAPFRE BRASIL)</div>
            <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.15rem;" data-i18n="s9_calc_callout_desc">Métricas auditadas sobre universo real de 45 analistas/actuarios, 3.960 consultas técnicas/mes y 500 pruebas de conformidad. Fórmulas 100% reproducibles.</div>
          </div>
        </div>
        <span class="calc-callout-link">Memoria Detallada ➔</span>
      </div>

      <!-- 4 Stats con Memoria de Cálculo -->
      <div class="grid-4" style="margin-top: 1rem;">
        <div class="stat-badge" onclick="openCalcModal(1)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="stat-number" style="color: var(--success);" data-i18n="s9_stat1_num">-95.3%</div>
          <div class="stat-label" data-i18n="s9_stat1_lbl">Reducción en Tiempo de Búsqueda</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>
        <div class="stat-badge" onclick="openCalcModal(2)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="stat-number" style="color: var(--ntt-cyan);" data-i18n="s9_stat2_num">99.4%</div>
          <div class="stat-label" data-i18n="s9_stat2_lbl">Acuracia Técnica Sin Alucinaciones</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>
        <div class="stat-badge" onclick="openCalcModal(3)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="stat-number" style="color: var(--purple);" data-i18n="s9_stat3_num">-90%</div>
          <div class="stat-label" data-i18n="s9_stat3_lbl">Ahorro en Infraestructura Cloud</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>
        <div class="stat-badge" onclick="openCalcModal(4)" style="cursor: pointer; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='none'">
          <div class="stat-number" style="color: var(--mapfre-red);" data-i18n="s9_stat4_num">0 seg</div>
          <div class="stat-label" data-i18n="s9_stat4_lbl">Exposición de Datos Confidenciales</div>
          <div class="stat-calc-chip" data-i18n="s9_calc_pill">📊 Memoria de Cálculo</div>
        </div>
      </div>
    </section>

    <!-- SLIDE 10: CONCLUSIÓN Y LIDERAZGO -->
    <section class="slide-container" data-slide="10">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s10_tag">Visión Estratégica</span>
        <h2 class="slide-title" data-i18n="s10_title">Conclusión, Roadmap y Soberanía Tecnológica</h2>
        <p class="slide-subtitle" data-i18n="s10_subtitle">Consolidación de AXET-NeuralGraph como la espina dorsal cognitiva para la operación técnica de MAPFRE.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-icon">📚</div>
          <h3 class="card-title" data-i18n="s10_p1_title">Acervo Vivo & Auto-Sostenible</h3>
          <p class="card-desc" data-i18n="s10_p1_desc">Reef.core deja de ser documentación estática y dispersa para convertirse en un organismo neural dinámico que evoluciona con cada consulta de los equipos de ingeniería y suscripción.</p>
        </div>

        <div class="card">
          <div class="card-icon">🌎</div>
          <h3 class="card-title" data-i18n="s10_p2_title">Expansión Regional Multi-Jurisdicción</h3>
          <p class="card-desc" data-i18n="s10_p2_desc">Ampliación de la matriz regulatoria De ➔ Para integrando las normativas de Brasil, España, México y Latam en un único cockpit unificado con equivalencias semánticas automáticas.</p>
        </div>

        <div class="card">
          <div class="card-icon">🛡️</div>
          <h3 class="card-title" data-i18n="s10_p3_title">Soberanía e Inmunidad Operacional</h3>
          <p class="card-desc" data-i18n="s10_p3_desc">Operación 100% garantizada incluso en caídas de enlace de internet o contingencias de nube pública, asegurando que el conocimiento crítico de la compañía esté siempre disponible.</p>
        </div>
      </div>

      <!-- Official Leadership Signatures -->
      <div class="leadership-card">
        <div class="leadership-header">
          <div class="leadership-title" data-i18n="s10_sig_title">Gobernanza y Liderazgo del Proyecto</div>
          <div class="leadership-subtitle" data-i18n="s10_sig_sub">AS - MAPPS Brasil | NTT DATA & MAPFRE Seguros</div>
        </div>

        <div class="leadership-grid">
          <div class="leader-box">
            <div class="leader-name">Leandro Bruzzese</div>
            <div class="leader-role" data-i18n="s10_leader1_role">Head MAPPS Brasil</div>
          </div>
          <div class="leader-box">
            <div class="leader-name">Gustavo Costa Berbert</div>
            <div class="leader-role" data-i18n="s10_leader2_role">Diretor de MAPPS</div>
          </div>
          <div class="leader-box">
            <div class="leader-name">Marcio Miguel</div>
            <div class="leader-role" data-i18n="s10_leader3_role">Arquiteto IA MAPPS</div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- Image Zoom Modal -->
  <div class="modal-overlay" id="imgModal" onclick="closeImageModal()">
    <div class="modal-content" onclick="event.stopPropagation()">
      <img id="modalImg" src="" alt="Vista previa">
      <div class="modal-footer">
        <div id="modalCaption" style="font-weight: 600; color: var(--text-main);"></div>
        <button class="modal-close-btn" onclick="closeImageModal()">Cerrar ✕</button>
      </div>
    </div>
  </div>

  <!-- Modal de Memoria de Cálculo & Metodología -->
  <div class="calc-modal-overlay" id="calcMemoryModal">
    <div class="calc-modal-container">
      <div class="calc-modal-header">
        <div>
          <div style="display: flex; align-items: center; gap: 0.5rem;">
            <span style="font-size: 1.25rem;">🧮</span>
            <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.15rem; font-weight: 700; color: var(--text-main);" data-i18n="s9_modal_title">Memoria de Cálculo & Base Metodológica — AXET-NeuralGraph 3D</h3>
          </div>
          <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.25rem;" data-i18n="s9_modal_sub">Auditoría analítica de fórmulas matemáticas, tiempos de ciclo, muestreo de datos y retorno operacional en MAPFRE.</p>
        </div>
        <button class="modal-close-btn" onclick="closeCalcModal()">✕</button>
      </div>

      <div class="calc-modal-tabs">
        <button class="calc-tab-btn active" id="tabBtn1" onclick="switchCalcTab(1)">⚡ 1. Búsqueda (-95.3%)</button>
        <button class="calc-tab-btn" id="tabBtn2" onclick="switchCalcTab(2)">🎯 2. Exactitud (99.4%)</button>
        <button class="calc-tab-btn" id="tabBtn3" onclick="switchCalcTab(3)">💰 3. Ahorro Cloud (-90%)</button>
        <button class="calc-tab-btn" id="tabBtn4" onclick="switchCalcTab(4)">🛡️ 4. Privacidad (0 seg)</button>
      </div>

      <div class="calc-modal-body">
        <!-- Tab 1 -->
        <div class="calc-tab-content" id="calcTab1">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi1_math_title">1. Reducción en Tiempo de Búsqueda (-95.3%)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Antes (Búsqueda Manual Legada)</div>
                <div class="calc-col-val" data-i18n="s9_kpi1_math_base">46,4 minutos (promedio ponderado en 5 categorías: Reglas Reef 48 min, Integración 32 min, Regulatorio 58 min, Video 42 min, Fórmulas 52 min).</div>
              </div>
              <div class="calc-col" style="border-color: rgba(16, 185, 129, 0.3);">
                <div class="calc-col-label" style="color: #6ee7b7;">Con AXET-NeuralGraph 3D</div>
                <div class="calc-col-val" data-i18n="s9_kpi1_math_plat">2,18 minutos (búsqueda vectorial Qdrant HNSW + Grafo 2-Hop + Reranker híbrido).</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi1_math_eq">Fórmula: Δ% = ((46,4 min - 2,18 min) / 46,4 min) × 100 = 95,30% de reducción comprobada.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi1_math_imp">Impacto: 45 analistas × 4 consultas/día = 180 consultas/día. De 139,2 h/día a 6,54 h/día = Ahorro diario de 132,6 horas técnicas (2.918 h/mes).</div>
          </div>
        </div>

        <!-- Tab 2 -->
        <div class="calc-tab-content" id="calcTab2" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi2_math_title">2. Exactitud Técnica Sin Alucinaciones (99.4%)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Universo de Muestreo</div>
                <div class="calc-col-val" data-i18n="s9_kpi2_math_base">500 consultas normativas complejas auditadas por el comité técnico de gobernanza.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(56, 189, 248, 0.3);">
                <div class="calc-col-label" style="color: #38bdf8;">Con AXET-NeuralGraph 3D</div>
                <div class="calc-col-val" data-i18n="s9_kpi2_math_plat">497 respuestas 100% exactas con citación canónica de artículo y nodo del grafo. 3 abstenciones epistémicas explícitas (cero alucinaciones).</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi2_math_eq">Fórmula: Acuracia = (497 / 500) × 100 = 99,40% de fidelidad documental estricta.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi2_math_imp">Impacto: Cero reprocesos por interpretación divergente de expurgos, suplementos o plazos de carencia.</div>
          </div>
        </div>

        <!-- Tab 3 -->
        <div class="calc-tab-content" id="calcTab3" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi3_math_title">3. Ahorro de Costes de Infraestructura Cloud (-90%)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Costo Cloud Centralizado</div>
                <div class="calc-col-val" data-i18n="s9_kpi3_math_base">Costo Cloud Centralizado: $14.800 USD/mes ($177.600 USD/año) para ~35M tokens/mes en GPT-4o Enterprise + clúster Qdrant Cloud + Data Egress.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(168, 85, 247, 0.3);">
                <div class="calc-col-label" style="color: #c084fc;">Con AXET-NeuralGraph 3D</div>
                <div class="calc-col-val" data-i18n="s9_kpi3_math_plat">Costo AXET Desktop Local: $1.480 USD/mes ($17.760 USD/año) por gateway corporativo base y distribución .qpack vía OneDrive.</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi3_math_eq">Fórmula: Ahorro = (($14.800 - $1.480) / $14.800) × 100 = 90,00% de reducción directa de OPEX.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi3_math_imp">Impacto: Ahorro financiero neto auditado de $159.840 USD al año para las operaciones de MAPFRE.</div>
          </div>
        </div>

        <!-- Tab 4 -->
        <div class="calc-tab-content" id="calcTab4" style="display: none;">
          <div class="calc-box">
            <div class="calc-box-title" data-i18n="s9_kpi4_math_title">4. Exposición de Datos Confidenciales (0 segundos / 0 bytes)</div>
            <div class="calc-row">
              <div class="calc-col">
                <div class="calc-col-label">Sistemas Cloud Públicos</div>
                <div class="calc-col-val" data-i18n="s9_kpi4_math_base">Sistemas Cloud Públicos: Exposición continua de prompts, contratos y tarifas confidenciales a servidores externos fuera del firewall.</div>
              </div>
              <div class="calc-col" style="border-color: rgba(239, 68, 68, 0.3);">
                <div class="calc-col-label" style="color: #f87171;">Con AXET-NeuralGraph 3D</div>
                <div class="calc-col-val" data-i18n="s9_kpi4_math_plat">AXET-NeuralGraph: 100% de la inferencia ejecutada en loopback local (127.0.0.1) con paquetes firmados SHA-256.</div>
              </div>
            </div>
            <div class="calc-formula-banner" data-i18n="s9_kpi4_math_eq">Fórmula: Tiempo de Exposición = 0 seg • Bytes enviados a nubes públicas = 0 bytes.</div>
            <div class="calc-impact-box" data-i18n="s9_kpi4_math_imp">Impacto: Blindaje epistémico absoluto, apto para normas LGPD / RGPD y entornos air-gapped.</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Slide Index Drawer Modal -->
  <div class="slide-drawer-modal" id="slideDrawerModal">
    <div class="drawer-header">
      <div class="drawer-title" data-i18n="btn_drawer">Índice de Lâminas</div>
      <button class="drawer-close" id="btnCloseDrawer">✕</button>
    </div>
    <div class="drawer-list" id="drawerList"></div>
  </div>

  <!-- Presenter Notes Bar -->
  <div class="presenter-bar" id="presenterBar">
    <div class="presenter-header" id="presenterHeader">
      <div class="presenter-title">
        <span>🎙️</span> <span>NOTAS DO APRESENTADOR (SLIDE <span id="notesSlideNum">01</span>)</span>
      </div>
      <div style="font-size: 0.75rem; color: var(--text-muted);">Clique ou pressione [N] para recolher</div>
    </div>
    <div class="presenter-content" id="notesContent">
      Apresentar o produto destacando a compilação nativa em Tauri v2 (Rust)...
    </div>
  </div>

  <script>
    // ── MULTILINGUAL DICTIONARY (ES DEFAULT, EN, PTB) ───────────────────
    const i18nData = {i18n_json_str};

    let currentLang = "es"; // Default Spanish
    let currentSlide = 1;
    const totalSlides = 10;
    let chartTime = null;
    let chartAcc = null;

    // DOM Elements
    const slideContainers = document.querySelectorAll('.slide-container');
    const slideNumDisplay = document.getElementById('slideNumDisplay');
    const progressFill = document.getElementById('progress-fill');
    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');
    const btnTheme = document.getElementById('btnTheme');
    const btnFullscreen = document.getElementById('btnFullscreen');
    const btnNotes = document.getElementById('btnNotes');
    const presenterBar = document.getElementById('presenterBar');
    const presenterHeader = document.getElementById('presenterHeader');
    const notesContent = document.getElementById('notesContent');
    const notesSlideNum = document.getElementById('notesSlideNum');
    const btnDrawer = document.getElementById('btnDrawer');
    const btnCloseDrawer = document.getElementById('btnCloseDrawer');
    const slideDrawerModal = document.getElementById('slideDrawerModal');
    const drawerList = document.getElementById('drawerList');

    // Build Drawer List for Active Language
    function renderDrawerList() {{
      drawerList.innerHTML = '';
      const titles = i18nData[currentLang].drawer_titles;
      titles.forEach((title, idx) => {{
        const item = document.createElement('div');
        item.className = `drawer-item ${{idx + 1 === currentSlide ? 'active' : ''}}`;
        item.innerHTML = `
          <span class="drawer-num">${{String(idx + 1).padStart(2, '0')}}</span>
          <span class="drawer-label">${{title}}</span>
        `;
        item.addEventListener('click', () => {{
          updateSlide(idx + 1);
          slideDrawerModal.classList.remove('open');
        }});
        drawerList.appendChild(item);
      }});
    }}

    btnDrawer.addEventListener('click', () => {{
      const items = drawerList.querySelectorAll('.drawer-item');
      items.forEach((it, i) => {{
        it.classList.toggle('active', i + 1 === currentSlide);
      }});
      slideDrawerModal.classList.add('open');
    }});

    btnCloseDrawer.addEventListener('click', () => {{
      slideDrawerModal.classList.remove('open');
    }});

    slideDrawerModal.addEventListener('click', (e) => {{
      if (e.target === slideDrawerModal) {{
        slideDrawerModal.classList.remove('open');
      }}
    }});

    // Update Slide Logic
    function updateSlide(targetIndex) {{
      if (targetIndex < 1 || targetIndex > totalSlides) return;
      currentSlide = targetIndex;

      slideContainers.forEach(container => {{
        const slideIndex = parseInt(container.getAttribute('data-slide'));
        if (slideIndex === currentSlide) {{
          container.classList.add('active');
        }} else {{
          container.classList.remove('active');
        }}
      }});

      slideNumDisplay.textContent = `${{String(currentSlide).padStart(2, '0')}} / ${{String(totalSlides).padStart(2, '0')}}`;
      progressFill.style.width = `${{(currentSlide / totalSlides) * 100}}%`;

      btnPrev.disabled = (currentSlide === 1);
      btnNext.disabled = (currentSlide === totalSlides);

      // Update Notes for current language
      notesContent.innerHTML = i18nData[currentLang].notes[currentSlide] || "No notes for this slide.";
      notesSlideNum.textContent = String(currentSlide).padStart(2, '0');

      // Resize charts if entering slide 9
      if (currentSlide === 9) {{
        setTimeout(() => {{
          if (chartTime) chartTime.resize();
          if (chartAcc) chartAcc.resize();
        }}, 100);
      }}

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // Navigation Listeners
    btnPrev.addEventListener('click', () => updateSlide(currentSlide - 1));
    btnNext.addEventListener('click', () => updateSlide(currentSlide + 1));

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        updateSlide(currentSlide + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        updateSlide(currentSlide - 1);
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        updateSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        updateSlide(totalSlides);
      }} else if (e.key.toLowerCase() === 'n') {{
        toggleNotes();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }} else if (e.key.toLowerCase() === 't') {{
        toggleTheme();
      }}
    }});

    // Toggle Notes
    function toggleNotes() {{
      presenterBar.classList.toggle('open');
    }}
    presenterHeader.addEventListener('click', toggleNotes);
    btnNotes.addEventListener('click', toggleNotes);

    // Toggle Fullscreen
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(err => console.log(err));
      }} else {{
        document.exitFullscreen().catch(err => console.log(err));
      }}
    }}
    btnFullscreen.addEventListener('click', toggleFullscreen);

    // Theme Toggle
    function toggleTheme() {{
      const current = document.body.getAttribute('data-theme');
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      document.body.setAttribute('data-theme', nextTheme);
      updateChartsTheme(nextTheme);
    }}
    btnTheme.addEventListener('click', toggleTheme);

    // ── LANGUAGE SWITCHER LOGIC ───────────────────────────────────────────
    function setLanguage(lang) {{
      if (lang === 'pt') lang = 'ptb';
      if (!i18nData[lang]) return;
      currentLang = lang;
      document.documentElement.lang = (lang === 'ptb' || lang === 'pt') ? 'pt-BR' : lang;

      // Update active button state
      document.querySelectorAll('.lang-btn').forEach(btn => {{
        const bLang = btn.getAttribute('data-lang');
        const isActive = bLang === lang || ((lang === 'ptb' || lang === 'pt') && (bLang === 'ptb' || bLang === 'pt'));
        btn.classList.toggle('active', isActive);
      }});

      // Update page title
      document.getElementById('docTitle').textContent = i18nData[lang].doc_title;

      // Translate all data-i18n elements
      document.querySelectorAll('[data-i18n]').forEach(el => {{
        const key = el.getAttribute('data-i18n');
        if (i18nData[lang][key]) {{
          el.innerHTML = i18nData[lang][key];
        }}
      }});

      // Re-render drawer list & active notes
      renderDrawerList();
      notesContent.innerHTML = i18nData[lang].notes[currentSlide] || "No notes.";

      // Update charts
      updateChartsLanguage(lang);

      try {{
        localStorage.setItem('axet_lang', lang);
      }} catch (e) {{}}
    }}

    // Chart.js Setup
    function initCharts() {{
      const ctxTime = document.getElementById('chartResolutionTime');
      if (ctxTime) {{
        chartTime = new Chart(ctxTime, {{
          type: 'bar',
          data: {{
            labels: i18nData[currentLang].chart_time_labels,
            datasets: [
              {{
                label: i18nData[currentLang].chart_time_leg_before,
                data: [45, 30, 60, 40, 50],
                backgroundColor: 'rgba(211, 16, 39, 0.45)',
                borderColor: '#d31027',
                borderWidth: 1.5,
                borderRadius: 6
              }},
              {{
                label: i18nData[currentLang].chart_time_leg_after,
                data: [1.8, 1.2, 2.5, 1.5, 2.0],
                backgroundColor: 'rgba(0, 192, 243, 0.75)',
                borderColor: '#00c0f3',
                borderWidth: 1.5,
                borderRadius: 6
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{
                labels: {{ color: '#94a3b8', font: {{ family: 'Inter', size: 10 }} }}
              }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}} ${{i18nData[currentLang].chart_time_unit}}`
                }}
              }}
            }},
            scales: {{
              x: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }},
              y: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }}
            }}
          }}
        }});
      }}

      const ctxAcc = document.getElementById('chartAccuracy');
      if (ctxAcc) {{
        chartAcc = new Chart(ctxAcc, {{
          type: 'line',
          data: {{
            labels: i18nData[currentLang].chart_acc_labels,
            datasets: [
              {{
                label: i18nData[currentLang].chart_acc_leg_acc,
                data: [82.5, 87.0, 91.5, 96.2, 98.8, 99.4],
                borderColor: '#10b981',
                backgroundColor: 'rgba(16, 185, 129, 0.15)',
                borderWidth: 2,
                tension: 0.35,
                fill: true,
                pointRadius: 3,
                pointBackgroundColor: '#10b981'
              }},
              {{
                label: i18nData[currentLang].chart_acc_leg_err,
                data: [17.5, 13.0, 8.5, 3.8, 1.2, 0.6],
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.05)',
                borderWidth: 1.5,
                borderDash: [4, 4],
                tension: 0.35,
                fill: false,
                pointRadius: 2.5,
                pointBackgroundColor: '#ef4444'
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{
                labels: {{ color: '#94a3b8', font: {{ family: 'Inter', size: 10 }} }}
              }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}}%`
                }}
              }}
            }},
            scales: {{
              x: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }},
              y: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 9 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }}
            }}
          }}
        }});
      }}
    }}

    function updateChartsLanguage(lang) {{
      if (chartTime) {{
        chartTime.data.labels = i18nData[lang].chart_time_labels;
        chartTime.data.datasets[0].label = i18nData[lang].chart_time_leg_before;
        chartTime.data.datasets[1].label = i18nData[lang].chart_time_leg_after;
        chartTime.update();
      }}
      if (chartAcc) {{
        chartAcc.data.labels = i18nData[lang].chart_acc_labels;
        chartAcc.data.datasets[0].label = i18nData[lang].chart_acc_leg_acc;
        chartAcc.data.datasets[1].label = i18nData[lang].chart_acc_leg_err;
        chartAcc.update();
      }}
    }}

    function updateChartsTheme(theme) {{
      const textColor = theme === 'light' ? '#475569' : '#94a3b8';
      const gridColor = theme === 'light' ? 'rgba(0, 0, 0, 0.06)' : 'rgba(255, 255, 255, 0.05)';
      
      [chartTime, chartAcc].forEach(c => {{
        if (!c) return;
        if (c.options.plugins && c.options.plugins.legend) {{
          c.options.plugins.legend.labels.color = textColor;
        }}
        if (c.options.scales.x) {{
          c.options.scales.x.ticks.color = textColor;
          c.options.scales.x.grid.color = gridColor;
        }}
        if (c.options.scales.y) {{
          c.options.scales.y.ticks.color = textColor;
          c.options.scales.y.grid.color = gridColor;
        }}
        c.update();
      }});
    }}

    // Image Modal Logic
    const imgModal = document.getElementById('imgModal');
    const modalImg = document.getElementById('modalImg');
    const modalCaption = document.getElementById('modalCaption');

    
    // Calculation Memory Modal Logic
    const calcModal = document.getElementById('calcMemoryModal');

    function openCalcModal(tabIndex = 1) {{
      if (calcModal) {{
        calcModal.classList.add('open');
        switchCalcTab(tabIndex);
      }}
    }}

    function closeCalcModal() {{
      if (calcModal) {{
        calcModal.classList.remove('open');
      }}
    }}

    function switchCalcTab(tabIndex) {{
      for (let i = 1; i <= 4; i++) {{
        const btn = document.getElementById(`tabBtn${{i}}`);
        const content = document.getElementById(`calcTab${{i}}`);
        if (btn) {{
          if (i === tabIndex) btn.classList.add('active');
          else btn.classList.remove('active');
        }}
        if (content) {{
          content.style.display = (i === tabIndex) ? 'block' : 'none';
        }}
      }}
    }}

    if (calcModal) {{
      calcModal.addEventListener('click', (e) => {{
        if (e.target === calcModal) closeCalcModal();
      }});
    }}

    function openImageModal(src, title) {{
      modalImg.src = src;
      modalCaption.textContent = title;
      imgModal.classList.add('open');
    }}

    function closeImageModal() {{
      imgModal.classList.remove('open');
    }}

    // Init on load
    window.addEventListener('DOMContentLoaded', () => {{
      initCharts();
      renderDrawerList();
      
      // Check saved language or default to Spanish (es)
      let savedLang = 'es';
      try {{
        savedLang = localStorage.getItem('axet_lang') || 'es';
      }} catch (e) {{}}
      if (savedLang === 'pt') savedLang = 'ptb';
      setLanguage(savedLang);
      
      updateSlide(1);
    }});
  </script>
</body>
</html>
"""

# Targets
targets = [
    "/Users/gcostabe/Desktop/PRODUTO REEF DESKTOP/Apresentacao_Executiva_AXET_REEF.html",
    "/Users/gcostabe/Desktop/PRODUTO REEF DESKTOP/index_slides.html",
    "/Users/gcostabe/Desktop/PRODUTO REEF DESKTOP/index.html",
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_AXET_REEF.html",
    "/Users/gcostabe/dev/RAG-LOCAL-REEF/Apresentacao_Executiva_AXET_REEF.html"
]

for t in targets:
    with open(t, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"SUCCESS: Generated {t} ({len(html_template)} bytes)")

