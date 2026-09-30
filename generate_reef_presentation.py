import os
import base64
import json
import subprocess

# Read base64 logos
with open("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_mapfre.png", "rb") as f:
    b64_mapfre = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")
with open("/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/assets/logo_nttdata.png", "rb") as f:
    b64_ntt = "data:image/png;base64," + base64.b64encode(f.read()).decode("ascii")

# Define the complete multilingual dictionary
i18n = {
    "es": {
        "doc_title": "AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA",
        "topbar_title_tag": "Plataforma Cognitiva Desktop",
        "topbar_subtitle": "RAG Local-First Estricto • Grafo 3D • Cero Fuga de Datos (Air-Gapped)",
        "nav_prev": "◀ Anterior",
        "nav_next": "Siguiente ▶",
        "btn_notes": "Notas [N]",
        "btn_drawer": "Índice",

        # Slide 1
        "s1_badge1": "PRODUCTO DESKTOP NATIVO",
        "s1_badge2": "AIR-GAPPED READY",
        "s1_badge3": "THREE.JS WEBGL 60FPS",
        "s1_title": "AXET-NeuralGraph 3D",
        "s1_title_accent": "Plataforma Cognitiva Desktop para Reglas Técnicas & Acervos de Misión Crítica (Reef.core)",
        "s1_lead": "Ecosistema corporativo de inteligencia artificial soberana desarrollado por <strong>NTT DATA</strong> para <strong>MAPFRE</strong>. Combina un <strong>Grafo Neural Tridimensional anatómico en WebGL</strong>, <strong>RAG Local-First estricto</strong>, <strong>neuroplasticidad sintética en tiempo real</strong> y <strong>cero fuga de datos</strong> para transformar la consulta de manuales, contratos y directrices actuariales en una experiencia inmersiva e instantánea.",
        "s1_stat1_num": "3.111+",
        "s1_stat1_lbl": "Nodos en Malla Encefálica",
        "s1_stat2_num": "9.472+",
        "s1_stat2_lbl": "Sinapsis & Aristas Relacionales",
        "s1_stat3_num": "< 100 MB",
        "s1_stat3_lbl": "Consumo RAM (Tauri v2 Rust)",
        "s1_stat4_num": "100%",
        "s1_stat4_lbl": "Localhost Air-Gapped (Cero Nube)",
        "s1_cta": "Explorar Arquitectura y Pilares ➔",

        # Slide 2
        "s2_tag": "Diagnóstico Crítico",
        "s2_title": "El Reto Estratégico: Los Riesgos de las Soluciones Web Tradicionales",
        "s2_subtitle": "¿Por qué un producto desktop nativo de soberanía absoluta y no una aplicación web basada en nube pública?",
        "s2_p1_title": "Riesgo de Fuga de Datos y Cumplimiento",
        "s2_p1_desc": "Enviar reglas de negocio confidenciales, fórmulas técnicas de suscripción y contratos sensibles a endpoints de nubes públicas de terceros (como OpenAI o AWS públicos) viola directrices de cumplimiento y expone la propiedad intelectual de MAPFRE a riesgos legales y filtraciones.",
        "s2_p2_title": "Latencia Crítica e Inestabilidad de Red",
        "s2_p2_desc": "Las herramientas web tradicionales dependen de llamadas REST remotas con latencias de 3 a 8 segundos. En situaciones de atención en tiempo real o auditoría de apólices, las desconexiones interrumpen el flujo analítico de los actuarios e ingenieros.",
        "s2_p3_title": "Envenenamiento de Memoria (Data Poisoning)",
        "s2_p3_desc": "Los sistemas RAG web comunes sufren contaminación epistémica: cualquier archivo subido por un usuario en un chat puede indexarse de forma indiscriminada en la base vectorial corporativa, corrompiendo las respuestas para toda la compañía.",

        # Slide 3
        "s3_tag": "Ecosistema Cognitivo",
        "s3_title": "La Ventaja de AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos",
        "s3_subtitle": "Una arquitectura de ingeniería integral diseñada para velocidad, seguridad estricta y gobernanza distribuida.",
        "s3_c1_title": "1. Grafo Neural 3D Anatómico",
        "s3_c1_desc": "Malla encefálica tridimensional en WebGL (Three.js) con 3.111 nodos y 9.472 sinapsis distribuidos según la neuroanatomía humana real (Lóbulos Temporal, Frontal, Parietal, Occipital y Cerebelo).",
        "s3_c2_title": "2. Neuroplasticidad en Tiempo Real",
        "s3_c2_desc": "Auto-rectificación sintética instantánea. Cuando se detecta un error de razonamiento, el sistema muta la memoria creando nodos de aprendizaje que prevalecen sobre documentaciones legadas.",
        "s3_c3_title": "3. Federación Git Cero Permisos",
        "s3_c3_desc": "Colaboración distribuida sin credenciales de repositorio. Cientos de usuarios comparten sinapsis vía Outbox local e Issues etiquetadas, con releases empaquetados en < 2 segundos.",
        "s3_c4_title": "4. RAG Local-First Estricto",
        "s3_c4_desc": "Aislamiento total en localhost (127.0.0.1). Entrega de conocimiento por snapshots cifrados (.qpack) con verificación SHA-256 y blindaje epistémico ante adjuntos efímeros.",
        "s3_c5_title": "5. Chat Multimodal con Telemetría SSE",
        "s3_c5_desc": "Lectura nativa en memoria de PDFs corporativos, PPTs (incluyendo notas de orador) y DOCX, con visión computacional y streaming de estado en tiempo real vía Server-Sent Events.",
        "s3_c6_title": "6. Matriz Regulatoria & Glosario De ➔ Para",
        "s3_c6_desc": "Módulo administrativo que armoniza órganos reguladores por país (SUSEP Brasil, DGSFP España) con thesaurus semántico para equivalencia técnica y actuarial inmediata.",

        # Slide 4
        "s4_tag": "Cartografía Cognitiva",
        "s4_title": "Grafo Neural 3D: Estructura Encefálica de Misión Crítica",
        "s4_subtitle": "Navegación espacial interactiva a 60 FPS inspirada en la neuroanatomía del cerebro humano.",
        "s4_l1_title": "Lóbulo Temporal (36% del Grafo)",
        "s4_l1_desc": "Memoria declarativa y semántica profunda. Alberga los contratos maestros, apólices activas, especificaciones de Reef.core y el histórico consolidado de jurisprudencia.",
        "s4_l2_title": "Lóbulo Frontal (28% del Grafo)",
        "s4_l2_desc": "Corteza prefrontal ejecutiva. Orquesta la toma de decisiones, reglas de suscripción (DUP), gobernanza de riesgos y razonamiento lógico-matemático de tarificación.",
        "s4_l3_title": "Lóbulo Parietal (24% del Grafo)",
        "s4_l3_desc": "Integración sensorial y de conectividad técnica. Mapea endpoints de API, esquemas JSON, contratos de microservicios y sincronización con sistemas centrales.",
        "s4_l4_title": "Lóbulo Occipital & Cerebelo (12%)",
        "s4_l4_desc": "Procesamiento multimodal visual (diagramas técnicos, flujogramas de procesos) y control de telemetria motora en streaming SSE a alta tasa de refresco.",

        # Slide 5
        "s5_tag": "Soberanía & Seguridad",
        "s5_title": "RAG Local-First Estricto & Blindaje Epistémico",
        "s5_subtitle": "Cómo AXET garantiza inmunidad total contra fugas de datos y envenenamiento de memoria.",
        "s5_k1_title": "Aislamiento Inviolable en 127.0.0.1",
        "s5_k1_desc": "Todo el pipeline de búsqueda semántica, cálculo de embeddings densos y orquestación de prompts se ejecuta exclusivamente en el localhost del usuario. <strong>Ningún fragmento de texto abandona la máquina de trabajo.</strong>",
        "s5_k2_title": "Snapshots Vetoriales Compactados (.qpack)",
        "s5_k2_desc": "El conocimiento técnico de Reef.core no se distribuye como archivos de texto en disco, sino empaquetado en colecciones Qdrant binarias cifradas con hash SHA-256 verificado al inicio de la aplicación.",
        "s5_k3_title": "Blindaje Epistémico de Adjuntos",
        "s5_k3_desc": "Los archivos adjuntos al chat (PDFs de apólices, capturas de pantalla, planillas) tienen un ciclo de vida estrictamente efímero en RAM: <strong>tienen prohibido contaminar la memoria permanente</strong>, blindando el modelo contra data poisoning.",

        # Slide 6
        "s6_tag": "IA con Aprendizaje Continuo",
        "s6_title": "Neuroplasticidad Sintética: Auto-Rectificación en Tiempo Real",
        "s6_subtitle": "El agente que detecta incongruencias en su propio razonamiento y muta su memoria de forma inmediata.",
        "s6_s1_step": "PASO 01",
        "s6_s1_title": "Detección de Divergencia",
        "s6_s1_desc": "Al interactuar con el actuario o ingeniero, el modelo contrasta la consulta con la base consolidada y detecta si una premisa técnica o regla de negocio ha quedado desfasada.",
        "s6_s2_step": "PASO 02",
        "s6_s2_title": "Mutación Topológica del Grafo",
        "s6_s2_desc": "El sistema genera de forma autónoma un nuevo nodo `APRENDIZADO_COGNITIVO` y una arista `RETIFICA_CONCEITO` con peso matemático reforzado (2.5+) apuntando al concepto corregido.",
        "s6_s3_step": "PASO 03",
        "s6_s3_title": "Prevalencia Canónica Universal",
        "s6_s3_desc": "A partir de ese instante, cualquier consulta futura de la organización prioriza el nodo rectificado sobre la documentación histórica, eliminando el riesgo de errores reiterados.",

        # Slide 7
        "s7_tag": "Gobernanza Distribuida",
        "s7_title": "Federación Git Cero Permisos: Colaboración a Escala",
        "s7_subtitle": "Cientos de colaboradores sincronizando mejoras de conocimiento sin requerir credenciales en el repositorio de código.",
        "s7_f1_title": "1. Outbox Local Desacoplado",
        "s7_f1_desc": "Cada aprendizaje generado por el usuario se serializa localmente en su Outbox personal, sin exigir credenciales ni tokens de desarrollador en GitHub.",
        "s7_f2_title": "2. Sincronización vía Issues Públicas/Privadas",
        "s7_f2_desc": "El cliente desktop envía los paquetes de aprendizaje como GitHub Issues con la etiqueta `cognitive-learning`, manteniendo el código fuente blindado contra escritura.",
        "s7_f3_title": "3. Curaduría Central del Master Admin",
        "s7_f3_desc": "En el panel web administrativo, los líderes técnicos evalúan las propuestas, auditando el impacto en el grafo antes de aprobar la incorporación oficial.",
        "s7_f4_title": "4. Release Global en Menos de 2 Segundos",
        "s7_f4_desc": "El pipeline compila el nuevo snapshot binario y lo distribuye vía GitHub Releases. Todos los escritorios de MAPFRE se actualizan en segundo plano en instantes.",

        # Slide 8
        "s8_tag": "Experiencia de Usuario",
        "s8_title": "Galería de Pantallas Reales de la Aplicación Desktop",
        "s8_subtitle": "Interfaz de alto rendimiento diseñada en Tauri v2, Next.js y Three.js para la máxima agilidad operativa.",
        "s8_img1_title": "Grafo Neural 3D en WebGL",
        "s8_img1_desc": "Malla encefálica navegable con 3.111 nodos corticales.",
        "s8_img2_title": "Inspección de Nodos Semánticos",
        "s8_img2_desc": "Detalle técnico, sinapsis y autoridad de Reef Academy.",
        "s8_img3_title": "Asistente Cognitivo Inmersivo",
        "s8_img3_desc": "Copilot integrado directamente en el espacio neural 3D.",
        "s8_img4_title": "Chat con Streaming SSE",
        "s8_img4_desc": "Telemetría dinámica en tiempo real y soporte multimodal.",
        "s8_img5_title": "Dashboard con Okta SSO",
        "s8_img5_desc": "Acceso unificado con perfil corporativo y atajos rápidos.",
        "s8_img6_title": "Matriz Regulatoria Jurisdiccional",
        "s8_img6_desc": "Gestión de equivalencias normativas De ➔ Para (SUSEP / DGSFP).",

        # Slide 9
        "s9_tag": "Resultados Comprobados",
        "s9_title": "Métricas Operacionales & Benchmarks Mensurados",
        "s9_subtitle": "El impacto directo de AXET-NeuralGraph 3D en tiempo, costes, exactitud y seguridad para MAPFRE.",
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

        # Slide 10
        "s10_tag": "Visión Estratégica",
        "s10_title": "Conclusión, Roadmap y Soberanía Tecnológica",
        "s10_subtitle": "Consolidación de AXET-NeuralGraph como la espina dorsal cognitiva para la operación técnica de MAPFRE.",
        "s10_p1_title": "Acervo Vivo & Auto-Sostenible",
        "s10_p1_desc": "Reef.core deja de ser documentación estática y dispersa para convertirse en un organismo neural dinámico que evoluciona con cada consulta de los equipos de ingeniería y suscripción.",
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
            "02. Diagnóstico: Riesgos de la Nube Web",
            "03. Visión de la Solución: 6 Pilares",
            "04. Grafo Neural 3D y Lóbulos Corticales",
            "05. RAG Local-First y Blindaje Epistémico",
            "06. Neuroplasticidad y Auto-Rectificación",
            "07. Federación Git Cero Permisos",
            "08. Galería de Pantallas del Producto",
            "09. Benchmarks de Rendimiento y ROI",
            "10. Conclusión y Liderazgo Ejecutivo"
        ],

        # Presenter Notes
        "notes": {
            1: "Presentar el producto destacando que es un binario nativo desktop en Tauri v2 (Rust) y no una aplicación web común. Enfatizar la combinación de 3.111 nodos en WebGL y el aislamiento 100% localhost air-gapped para MAPFRE.",
            2: "Subrayar el dolor que motivó este desarrollo: los acervos de Reef.core no podían subirse a APIs de OpenAI o AWS por cuestiones de privacidad, confidencialidad y riesgos regulatorios de SUSEP y DGSFP.",
            3: "Explicar brevemente los 6 pilares, resaltando que la suma de neuroplasticidad en tiempo real y federación git cero permisos resuelve la actualización continua del conocimiento técnico.",
            4: "Detallar la neuroanatomía del grafo 3D: por qué el Lóbulo Temporal alberga los contratos y reglas de negocio, mientras el Frontal decide y el Parietal gestiona integraciones de microservicios.",
            5: "Explicar el concepto de 'Blindaje Epistémico'. Aclarar a la directiva cómo se evita el data poisoning: los archivos subidos al chat mueren con la sesión y nunca contaminan el grafo maestro.",
            6: "Demostrar cómo funciona la auto-rectificación: si un actuario señala un cambio normativo, el modelo muta su topología generando un nodo de aprendizaje canónico con peso reforzado.",
            7: "Destacar la elegancia del mecanismo de federación: los colaboradores sincronizan conocimientos a través de Issues de GitHub sin comprometer tokens ni permisos de escritura en el código.",
            8: "Pasearse por las pantallas reales del sistema. Mencionar la integración con Okta SSO y el streaming SSE que sustituye a los puntos de carga por telemetría exacta en tiempo real.",
            9: "Resaltar el gráfico de tiempo: pasar de 45 minutos a 2 minutos en la resolución de consultas complejas representa un salto de productividad del 95% para los equipos de suscripción y soporte.",
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
    },

    "en": {
        "doc_title": "AXET-NeuralGraph 3D | Cognitive Desktop Platform — MAPFRE & NTT DATA",
        "topbar_title_tag": "Cognitive Desktop Platform",
        "topbar_subtitle": "Strict Local-First RAG • 3D Neural Graph • Zero Data Leakage (Air-Gapped)",
        "nav_prev": "◀ Previous",
        "nav_next": "Next ▶",
        "btn_notes": "Notes [N]",
        "btn_drawer": "Index",

        # Slide 1
        "s1_badge1": "NATIVE DESKTOP PRODUCT",
        "s1_badge2": "AIR-GAPPED READY",
        "s1_badge3": "THREE.JS WEBGL 60FPS",
        "s1_title": "AXET-NeuralGraph 3D",
        "s1_title_accent": "Cognitive Desktop Platform for Technical Rules & Mission-Critical Repositories (Reef.core)",
        "s1_lead": "Sovereign enterprise AI ecosystem developed by <strong>NTT DATA</strong> for <strong>MAPFRE</strong>. Combines an <strong>anatomical 3D Neural Graph in WebGL</strong>, <strong>strict Local-First RAG</strong>, <strong>real-time synthetic neuroplasticity</strong>, and <strong>zero data leakage</strong> to transform documentation and underwriting guidelines into an immersive, instant experience.",
        "s1_stat1_num": "3,111+",
        "s1_stat1_lbl": "Brain Mesh Semantic Nodes",
        "s1_stat2_num": "9,472+",
        "s1_stat2_lbl": "Synapses & Relational Edges",
        "s1_stat3_num": "< 100 MB",
        "s1_stat3_lbl": "RAM Footprint (Tauri v2 Rust)",
        "s1_stat4_num": "100%",
        "s1_stat4_lbl": "Localhost Air-Gapped (Zero Cloud)",
        "s1_cta": "Explore Architecture & Pillars ➔",

        # Slide 2
        "s2_tag": "Critical Diagnostic",
        "s2_title": "The Strategic Challenge: Risks of Traditional Web Cloud Solutions",
        "s2_subtitle": "Why a native desktop application with absolute data sovereignty rather than a public cloud web app?",
        "s2_p1_title": "Data Leakage and Regulatory Risk",
        "s2_p1_desc": "Streaming confidential business rules, underwriting formulas, and policy contracts to public third-party cloud APIs (such as public OpenAI or AWS) breaches regulatory compliance and exposes proprietary IP.",
        "s2_p2_title": "Critical Latency and Network Dependency",
        "s2_p2_desc": "Web-based AI tools rely on remote REST endpoints with 3-8 second latencies. During real-time underwriting reviews or actuarial audits, network drops sever critical analytical workflows.",
        "s2_p3_title": "Epistemic Memory Poisoning",
        "s2_p3_desc": "Standard cloud RAG systems suffer from data poisoning: files uploaded by single users into chats can be inadvertently vectorized into the global corpus, degrading answer quality company-wide.",

        # Slide 3
        "s3_tag": "Cognitive Ecosystem",
        "s3_title": "The AXET-NeuralGraph Desktop Advantage: 6 Technological Pillars",
        "s3_subtitle": "A full-stack engineering suite built for speed, airtight data privacy, and distributed governance.",
        "s3_c1_title": "1. Anatomical 3D Neural Graph",
        "s3_c1_desc": "Real-time 60 FPS WebGL brain mesh with 3,111 nodes and 9,472 synapses organized across human brain lobes (Temporal, Frontal, Parietal, Occipital, and Cerebellum).",
        "s3_c2_title": "2. Real-Time Neuroplasticity",
        "s3_c2_desc": "Synthetic self-rectification. When reasoning gaps occur, the agent mutates its memory creating permanent learning nodes that supersede obsolete documentation.",
        "s3_c3_title": "3. Zero-Permission Git Federation",
        "s3_c3_desc": "Distributed collaboration without repository credentials. Hundreds of users share synapses via local Outbox and tagged Issues, with release bundles deployed in < 2 seconds.",
        "s3_c4_title": "4. Strict Local-First RAG",
        "s3_c4_desc": "Total isolation on localhost (127.0.0.1). Knowledge delivered via encrypted binary snapshots (.qpack) with SHA-256 integrity checks and epistemic shielding.",
        "s3_c5_title": "5. Multimodal Chat with SSE Telemetry",
        "s3_c5_desc": "Native in-memory parsing of corporate PDFs, PPTs (including speaker notes), and DOCX, featuring computer vision and live Server-Sent Events status streaming.",
        "s3_c6_title": "6. Regulatory Matrix & Cross-Thesaurus",
        "s3_c6_desc": "Administrative module harmonizing multi-country insurance regulators (SUSEP Brazil, DGSFP Spain) with instant terminology equivalency tables.",

        # Slide 4
        "s4_tag": "Cognitive Cartography",
        "s4_title": "3D Neural Graph: Mission-Critical Encephalic Mapping",
        "s4_subtitle": "Interactive spatial navigation at 60 FPS inspired by human brain neuroanatomy.",
        "s4_l1_title": "Temporal Lobe (36% of Graph)",
        "s4_l1_desc": "Deep declarative and semantic memory. Hosts master insurance policies, contracts, Reef.core technical specifications, and legal precedents.",
        "s4_l2_title": "Frontal Lobe (28% of Graph)",
        "s4_l2_desc": "Executive prefrontal cortex. Orchestrates underwriting decision-making, DUP risk policies, governance rules, and actuarial mathematical logic.",
        "s4_l3_title": "Parietal Lobe (24% of Graph)",
        "s4_l3_desc": "Sensory and technical integration. Maps API endpoints, JSON payloads, microservice interface contracts, and core engine connectors.",
        "s4_l4_title": "Occipital & Cerebellum (12%)",
        "s4_l4_desc": "Visual multimodal processing (architectural schematics, process flowcharts) and low-latency SSE motor streaming telemetry.",

        # Slide 5
        "s5_tag": "Sovereignty & Security",
        "s5_title": "Strict Local-First RAG & Epistemic Shielding",
        "s5_subtitle": "How AXET achieves 100% immunity against data leakage and memory contamination.",
        "s5_k1_title": "Inviolable 127.0.0.1 Localhost Isolation",
        "s5_k1_desc": "The entire semantic search pipeline, dense embedding computations, and LLM prompt orchestrations run strictly on the user machine. <strong>No raw text ever leaves the workstation.</strong>",
        "s5_k2_title": "Compact Vector Snapshots (.qpack)",
        "s5_k2_desc": "Reef.core technical documentation is never stored as loose disk files, but packaged in binary encrypted Qdrant collections verified with SHA-256 hashes at boot time.",
        "s5_k3_title": "Epistemic Shielding on Attachments",
        "s5_k3_desc": "Files attached to user chats (policy PDFs, screenshots, spreadsheets) live transiently in RAM: <strong>they are strictly prohibited from writing to permanent memory</strong>, preventing data poisoning.",

        # Slide 6
        "s6_tag": "Continuous Learning AI",
        "s6_title": "Synthetic Neuroplasticity: Real-Time Self-Correction",
        "s6_subtitle": "The agent that detects flaws in its own reasoning and immediately mutates its knowledge structure.",
        "s6_s1_step": "STEP 01",
        "s6_s1_title": "Divergence Detection",
        "s6_s1_desc": "During user dialogues, the agent cross-checks queries with the canonical corpus and detects if an actuarial formula or technical rule has changed.",
        "s6_s2_step": "STEP 02",
        "s6_s2_title": "Topological Graph Mutation",
        "s6_s2_desc": "The engine autonomously creates a new `APRENDIZADO_COGNITIVO` node connected via a reinforced `RETIFICA_CONCEITO` edge with a 2.5+ mathematical weight.",
        "s6_s3_step": "STEP 03",
        "s6_s3_title": "Universal Canonical Precedence",
        "s6_s3_desc": "From that moment on, all future queries across the enterprise prioritize the rectified node over legacy documentation, eliminating repetitive hallucinations.",

        # Slide 7
        "s7_tag": "Distributed Governance",
        "s7_title": "Zero-Permission Git Federation: Scale Across Teams",
        "s7_subtitle": "Hundreds of collaborators synchronizing technical insights without needing write permissions on the codebase.",
        "s7_f1_title": "1. Decoupled Local Outbox",
        "s7_f1_desc": "Each cognitive learning entry is queued locally in the user personal Outbox, without developer logins or GitHub write tokens.",
        "s7_f2_title": "2. Synchronization via Tagged Issues",
        "s7_f2_desc": "The desktop client transmits approved synaptic updates as GitHub Issues with the `cognitive-learning` label, keeping the repository secure.",
        "s7_f3_title": "3. Master Admin Curatorship",
        "s7_f3_desc": "On the web administration console, technical leads review proposed updates, verifying topological impact before merging.",
        "s7_f4_title": "4. Global Release in Under 2 Seconds",
        "s7_f4_desc": "The CI pipeline builds the consolidated binary snapshot and deploys it via GitHub Releases, updating desktop clients instantaneously.",

        # Slide 8
        "s8_tag": "User Experience",
        "s8_title": "Real Application Screen Gallery",
        "s8_subtitle": "High-performance interface built in Tauri v2, Next.js, and Three.js for maximum actuarial and engineering speed.",
        "s8_img1_title": "3D WebGL Neural Graph",
        "s8_img1_desc": "Interactive brain mesh with 3,111 cortical nodes.",
        "s8_img2_title": "Semantic Node Inspection",
        "s8_img2_desc": "Technical metadata, synapses, and Reef Academy authority.",
        "s8_img3_title": "Immersive Cognitive Assistant",
        "s8_img3_desc": "Copilot embedded seamlessly inside the 3D neural space.",
        "s8_img4_title": "SSE Streaming Chat",
        "s8_img4_desc": "Dynamic real-time telemetry replacing loading spinners.",
        "s8_img5_title": "Okta SSO Dashboard",
        "s8_img5_desc": "Enterprise corporate profile with instant query shortcuts.",
        "s8_img6_title": "Regulatory Matrix Console",
        "s8_img6_desc": "Jurisdictional cross-reference management (SUSEP / DGSFP).",

        # Slide 9
        "s9_tag": "Proven Results",
        "s9_title": "Measured Operational Impacts & Benchmarks",
        "s9_subtitle": "Direct measurable value delivered by AXET-NeuralGraph Desktop in time, cost, accuracy, and data security.",
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

        # Slide 10
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
            "02. Diagnostic: Web Cloud AI Risks",
            "03. Solution Vision: 6 Pillars",
            "04. 3D Neural Graph & Cortical Lobes",
            "05. Local-First RAG & Epistemic Shield",
            "06. Synthetic Neuroplasticity",
            "07. Zero-Permission Git Federation",
            "08. Desktop Application Screen Gallery",
            "09. Performance Benchmarks & ROI",
            "10. Conclusion & Executive Leadership"
        ],

        # Presenter Notes
        "notes": {
            1: "Introduce the product highlighting its native desktop binary build in Tauri v2 (Rust). Emphasize the WebGL 3D graph with 3,111 nodes and 100% air-gapped security for MAPFRE.",
            2: "Highlight the business challenge: Reef.core documents could not be sent to external cloud APIs due to strict privacy, confidentiality, and insurance regulations (SUSEP / DGSFP).",
            3: "Walk through the 6 pillars, noting that combining real-time neuroplasticity with zero-permission Git federation enables scalable, continuous knowledge updates.",
            4: "Explain the brain lobe architecture: why the Temporal Lobe hosts contracts and business rules, while the Frontal Lobe makes underwriting decisions and the Parietal Lobe handles APIs.",
            5: "Introduce 'Epistemic Shielding'. Reassure executive stakeholders that chat attachments are transient in RAM and strictly prevented from contaminating permanent vector memory.",
            6: "Explain self-correction: when an actuary corrects a rule, the agent rewrites its topological memory, creating a permanent learning node with 2.5+ weight.",
            7: "Highlight the elegant Git federation: users share technical discoveries via GitHub Issues without exposing code repository write permissions or secret tokens.",
            8: "Present the high-resolution screenshots. Mention Okta SSO and the SSE telemetry status that replaces generic loading spinners with millisecond precision.",
            9: "Focus on the ROI benchmark: slashing technical inquiry resolution from 45 minutes to 2 minutes delivers a 95% productivity leap for engineering and underwriting.",
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
    },

    "ptb": {
        "doc_title": "AXET-NeuralGraph 3D | Plataforma Cognitiva Desktop — MAPFRE & NTT DATA",
        "topbar_title_tag": "Plataforma Cognitiva Desktop",
        "topbar_subtitle": "RAG Local-First Estrito • Grafo 3D • Zero Vazamento de Dados (Air-Gapped)",
        "nav_prev": "◀ Anterior",
        "nav_next": "Próximo ▶",
        "btn_notes": "Notas [N]",
        "btn_drawer": "Índice",

        # Slide 1
        "s1_badge1": "PRODUTO DESKTOP NATIVO",
        "s1_badge2": "AIR-GAPPED READY",
        "s1_badge3": "THREE.JS WEBGL 60FPS",
        "s1_title": "AXET-NeuralGraph 3D",
        "s1_title_accent": "Plataforma Cognitiva Desktop para Regras Técnicas & Acervos de Missão Crítica (Reef.core)",
        "s1_lead": "Ecossistema corporativo de inteligência artificial soberana desenvolvido pela <strong>NTT DATA</strong> para a <strong>MAPFRE</strong>. Combina um <strong>Grafo Neural Tridimensional anatômico em WebGL</strong>, <strong>RAG Local-First estrito</strong>, <strong>neuroplasticidade sintética em tempo real</strong> e <strong>zero vazamento de dados</strong> para transformar a consulta a manuais, apólices e regras atuariais em uma experiência imersiva e instantânea.",
        "s1_stat1_num": "3.111+",
        "s1_stat1_lbl": "Nós Semânticos na Malha Cerebral",
        "s1_stat2_num": "9.472+",
        "s1_stat2_lbl": "Sinapses & Conexões Relacionais",
        "s1_stat3_num": "< 100 MB",
        "s1_stat3_lbl": "Consumo de RAM (Tauri v2 Rust)",
        "s1_stat4_num": "100%",
        "s1_stat4_lbl": "Localhost Air-Gapped (Zero Nuvem)",
        "s1_cta": "Explorar Arquitetura e Pilares ➔",

        # Slide 2
        "s2_tag": "Diagnóstico Crítico",
        "s2_title": "O Desafio Estratégico: Riscos das Soluções Web Tradicionais",
        "s2_subtitle": "Por que um produto desktop nativo de soberania absoluta e não uma aplicação web baseada em nuvem pública?",
        "s2_p1_title": "Risco de Vazamento de Dados e Não Conformidade",
        "s2_p1_desc": "Enviar regras de negócio confidenciais, fórmulas de subscrição e contratos de apólices a endpoints de nuvem pública (como OpenAI ou AWS) viola diretrizes de compliance e expõe a propriedade intelectual da MAPFRE a riscos legais e vazamentos.",
        "s2_p2_title": "Latência Crítica e Dependência de Conexão",
        "s2_p2_desc": "Ferramentas web tradicionais dependem de chamadas de rede com latência de 3 a 8 segundos. Em análises atuariais ou emissão de apólices em tempo real, oscilações de rede interrompem o fluxo de trabalho dos especialistas.",
        "s2_p3_title": "Envenenamento de Memória (Data Poisoning)",
        "s2_p3_desc": "Sistemas RAG em nuvem sofrem contaminação epistêmica: arquivos anexados por um usuário em chats podem ser indevidamente vetorizados na base permanente, degradando as respostas para toda a companhia.",

        # Slide 3
        "s3_tag": "Ecossistema Cognitivo",
        "s3_title": "A Vantagem do AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos",
        "s3_subtitle": "Uma arquitetura de engenharia de ponta a ponta projetada para velocidade, privacidade estrita e governança colaborativa.",
        "s3_c1_title": "1. Grafo Neural 3D Anatômico",
        "s3_c1_desc": "Malha encefálica tridimensional em WebGL (Three.js) com 3.111 nós e 9.472 sinapses distribuídos conforme a neuroanatomia humana real (Lobos Temporal, Frontal, Parietal, Occipital e Cerebelo).",
        "s3_c2_title": "2. Neuroplasticidade em Tempo Real",
        "s3_c2_desc": "Auto-retificação sintética instantânea. Quando o assistente detecta uma falha de raciocínio, ele muta a estrutura vetorial criando nós de aprendizado canônicos que prevalecem sobre normas legadas.",
        "s3_c3_title": "3. Federação Git Zero Permissões",
        "s3_c3_desc": "Colaboração distribuída sem credenciais no repositório. Centenas de usuários compartilham sinapses via Outbox local e Issues etiquetadas, com releases de pacotes em menos de 2 segundos.",
        "s3_c4_title": "4. RAG Local-First Estrito",
        "s3_c4_desc": "Isolamento total no localhost (127.0.0.1). Entrega de conhecimento por snapshots compactados (.qpack) com verificação SHA-256 e blindagem epistêmica contra anexos efêmeros.",
        "s3_c5_title": "5. Chat Multimodal com Telemetria SSE",
        "s3_c5_desc": "Leitura nativa em memória de PDFs corporativos, PPTs (com anotações de slide) e DOCX, com visão computacional e telemetria de status em tempo real via Server-Sent Events.",
        "s3_c6_title": "6. Matriz Regulatória & Glossário De ➔ Para",
        "s3_c6_desc": "Módulo administrativo que conecta órgãos reguladores por jurisdição (SUSEP Brasil, DGSFP Espanha) com thesaurus semântico para equivalência técnica e atuarial imediata.",

        # Slide 4
        "s4_tag": "Cartografia Cognitiva",
        "s4_title": "Grafo Neural 3D: Estrutura Encefálica de Missão Crítica",
        "s4_subtitle": "Navegação espacial interativa a 60 FPS inspirada na neuroanatomia do cérebro humano.",
        "s4_l1_title": "Lobo Temporal (36% do Grafo)",
        "s4_l1_desc": "Memória declarativa e semântica profunda. Armazena os contratos mestres, apólices ativas, especificações do Reef.core e histórico consolidado de diretrizes.",
        "s4_l2_title": "Lobo Frontal (28% do Grafo)",
        "s4_l2_desc": "Córtex pré-frontal executivo. Orquestra a tomada de decisões, regras de subscrição (DUP), governança de riscos e raciocínio lógico-matemático de tarifação.",
        "s4_l3_title": "Lobo Parietal (24% do Grafo)",
        "s4_l3_desc": "Integração sensorial e conectividade técnica. Mapeia endpoints de API, esquemas JSON de integração, contratos de microserviços e barramentos corporativos.",
        "s4_l4_title": "Lobo Occipital & Cerebelo (12%)",
        "s4_l4_desc": "Processamento multimodal visual (diagramas técnicos, fluxogramas de processos) e controle de telemetria motora em streaming SSE a alta taxa de atualização.",

        # Slide 5
        "s5_tag": "Soberania & Segurança",
        "s5_title": "RAG Local-First Estrito & Blindagem Epistêmica",
        "s5_subtitle": "Como o AXET garante imunidade contra vazamento de dados e envenenamento de memória.",
        "s5_k1_title": "Isolamento Inviolável em 127.0.0.1",
        "s5_k1_desc": "Todo o pipeline de busca vetorial, cálculo de embeddings densos e orquestração de prompts roda exclusivamente no localhost da estação de trabalho. <strong>Nenhum fragmento de texto sai da máquina.</strong>",
        "s5_k2_title": "Snapshots Vetoriais Compactados (.qpack)",
        "s5_k2_desc": "O acervo do Reef.core não é distribuído em arquivos de texto plano, mas compactado em coleções binárias do Qdrant verificadas por hash SHA-256 na inicialização do app.",
        "s5_k3_title": "Blindagem Epistêmica de Anexos",
        "s5_k3_desc": "Arquivos anexados a chats (PDFs de apólices, capturas de tela, planilhas) têm ciclo de vida efêmero em RAM: <strong>são proibidos de gravar na memória permanente</strong>, blindando contra data poisoning.",

        # Slide 6
        "s6_tag": "IA com Aprendizado Contínuo",
        "s6_title": "Neuroplasticidade Sintética: Auto-Retificação em Tempo Real",
        "s6_subtitle": "O assistente que detecta falhas em seu próprio raciocínio e muta sua memória instantaneamente.",
        "s6_s1_step": "PASSO 01",
        "s6_s1_title": "Detecção de Divergência",
        "s6_s1_desc": "Durante a conversa com o especialista atuarial ou técnico, o modelo confronta a consulta com o grafo consolidado e detecta se uma premissa técnica foi alterada.",
        "s6_s2_step": "PASO 02",
        "s6_s2_title": "Mutação Topológica do Grafo",
        "s6_s2_desc": "O sistema gera de forma autônoma um novo nó `APRENDIZADO_COGNITIVO` e uma aresta `RETIFICA_CONCEITO` com peso reforçado (2.5+) apontando para o conceito canônico corrigido.",
        "s6_s3_step": "PASSO 03",
        "s6_s3_title": "Prevalência Canônica Universal",
        "s6_s3_desc": "A partir desse instante, qualquer consulta futura da organização prioriza o nó retificado sobre documentações legadas, eliminando o erro recorrente.",

        # Slide 7
        "s7_tag": "Governança Distribuída",
        "s7_title": "Federação Git Zero Permissões: Colaboração em Escala",
        "s7_subtitle": "Centenas de colaboradores sincronizando aprendizados sem necessitar de permissões de escrita no repositório.",
        "s7_f1_title": "1. Outbox Local Desacoplado",
        "s7_f1_desc": "Cada aprendizado gerado pelo especialista é serializado no Outbox local da sua máquina, sem exigir logins ou tokens de desenvolvedor no GitHub.",
        "s7_f2_title": "2. Sincronização via Issues Etiquetadas",
        "s7_f2_desc": "O cliente desktop transmite os pacotes como GitHub Issues com o marcador `cognitive-learning`, mantendo a base de código 100% blindada contra escrita externa.",
        "s7_f3_title": "3. Curadoria Central do Master Admin",
        "s7_f3_desc": "No painel web administrativo, os líderes técnicos avaliam as propostas, auditando o impacto no grafo antes de aprovar a incorporação definitiva.",
        "s7_f4_title": "4. Release Global em Menos de 2 Segundos",
        "s7_f4_desc": "O pipeline compila o novo pacote binário (.pack) e o disponibiliza via GitHub Releases. Todos os clientes desktop MAPFRE se atualizam em segundo plano.",

        # Slide 8
        "s8_tag": "Experiência do Usuário",
        "s8_title": "Galeria de Telas Reais da Aplicação Desktop",
        "s8_subtitle": "Interface nativa desenvolvida em Tauri v2, Next.js e Three.js para máxima agilidade operacional.",
        "s8_img1_title": "Grafo Neural 3D em WebGL",
        "s8_img1_desc": "Malha cerebral interativa com 3.111 nós corticais a 60 FPS.",
        "s8_img2_title": "Inspeção de Nós Semânticos",
        "s8_img2_desc": "Metadados técnicos, sinapses e autoridade do Reef Academy.",
        "s8_img3_title": "Assistente Cognitivo Imersivo",
        "s8_img3_desc": "Copilot integrado diretamente ao espaço neural tridimensional.",
        "s8_img4_title": "Chat com Streaming SSE",
        "s8_img4_desc": "Telemetria dinâmica em tempo real substituindo esperas estáticas.",
        "s8_img5_title": "Dashboard com Okta SSO",
        "s8_img5_desc": "Perfil corporativo unificado com atalhos rápidos de consulta.",
        "s8_img6_title": "Matriz Regulatória Jurisdicional",
        "s8_img6_desc": "Gestão de equivalências normativas De ➔ Para (SUSEP / DGSFP).",

        # Slide 9
        "s9_tag": "Resultados Comprovados",
        "s9_title": "Métricas Operacionais & Benchmarks Mensurados",
        "s9_subtitle": "Impacto quantitativo do AXET-NeuralGraph 3D em tempo, custos, precisão e conformidade na MAPFRE.",
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

        # Slide 10
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
            "02. Diagnóstico: Riscos da Nuvem Web",
            "03. Visão da Solução: 6 Pilares",
            "04. Grafo Neural 3D e Lobos Corticais",
            "05. RAG Local-First e Blindagem Epistêmica",
            "06. Neuroplasticidade e Auto-Retificação",
            "07. Federação Git Zero Permissões",
            "08. Galeria de Telas do Produto",
            "09. Benchmarks de Desempenho e ROI",
            "10. Conclusão e Liderança Executiva"
        ],

        # Presenter Notes
        "notes": {
            1: "Apresentar o produto destacando a compilação nativa em Tauri v2 (Rust) e não uma aplicação web comum. Enfatizar a malha 3D com 3.111 nós em WebGL e a operação 100% localhost air-gapped para a MAPFRE.",
            2: "Sublinhar a motivação central: os acervos do Reef.core e regras de subscrição não podiam ser enviados a APIs de nuvem pública por razões de privacidade, compliance e sigilo atuarial.",
            3: "Explicar sucintamente os 6 pilares, reforçando como a neuroplasticidade em tempo real somada à federação git sem credenciais resolve a evolução do conhecimento técnico sem riscos de segurança.",
            4: "Detalhar a cartografia cortical: o Lobo Temporal armazena contratos e memórias semânticas, enquanto o Frontal decide e o Parietal integra microserviços e APIs.",
            5: "Explicar o 'Blindagem Epistêmica'. Esclarecer à diretoria que anexos temporários no chat não infectam a base permanente, garantindo imunidade total contra data poisoning.",
            6: "Demonstrar a neuroplasticidade sintética: ao corrigir uma diretriz, o agente cria um nó de aprendizado com peso 2.5+ que passa a ser a regra padrão para toda a companhia.",
            7: "Ressaltar o modelo de federação: especialistas colaboram via GitHub Issues etiquetadas, sem que ninguém precise de permissão de escrita ou token de desenvolvedor.",
            8: "Apresentar a galeria de telas reais em alta resolução. Destacar a integração com Okta SSO e a telemetria dinâmica via SSE que substitui telas de carregamento.",
            9: "Exaltar o salto de produtividade: redução no tempo médio de resolução técnica de 45 minutos para apenas 2 minutos (ganho superior a 95%).",
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
}

# Alias pt to ptb
i18n["pt"] = i18n["ptb"]

# Serialize i18n to valid JS
i18n_json_str = json.dumps(i18n, indent=2, ensure_ascii=False)

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
      --bg-card: rgba(15, 23, 42, 0.78);
      --bg-card-hover: rgba(22, 34, 61, 0.88);
      --bg-glass: rgba(255, 255, 255, 0.035);
      --border-color: rgba(255, 255, 255, 0.08);
      --border-highlight: rgba(0, 102, 255, 0.4);
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
      
      --shadow-lg: 0 20px 30px -10px rgba(0, 0, 0, 0.6), 0 8px 12px -6px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 25px rgba(0, 102, 255, 0.25);
      --transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    body[data-theme="light"] {{
      --bg-primary: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.92);
      --bg-card-hover: rgba(241, 245, 249, 0.95);
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
        radial-gradient(circle at 15% 15%, rgba(0, 102, 255, 0.08) 0%, transparent 45%),
        radial-gradient(circle at 85% 85%, rgba(0, 192, 243, 0.06) 0%, transparent 45%);
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
      padding: 0 2rem;
      z-index: 1000;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
      white-space: nowrap;
    }}

    .brand-group {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
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
      gap: 0.65rem;
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
      padding: 2.5rem 3.5rem 5rem 3.5rem;
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
      margin-bottom: 2rem;
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
      margin-bottom: 0.85rem;
    }}

    .slide-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.3rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.2;
      color: var(--text-main);
      margin-bottom: 0.65rem;
    }}

    .slide-title span.accent {{
      background: linear-gradient(135deg, var(--ntt-blue-light) 0%, var(--ntt-cyan) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .slide-subtitle {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.5;
      max-width: 1000px;
    }}

    /* Cards and Grids */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1.75rem;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1.5rem;
    }}

    .grid-4 {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.25rem;
    }}

    .card {{
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 1.75rem;
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
      background: linear-gradient(90deg, transparent, rgba(0, 102, 255, 0.4), transparent);
      opacity: 0;
      transition: var(--transition);
    }}

    .card:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-3px);
      box-shadow: var(--shadow-glow), var(--shadow-lg);
    }}

    .card:hover::before {{
      opacity: 1;
    }}

    .card-icon {{
      font-size: 1.85rem;
      margin-bottom: 1rem;
      width: 48px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 12px;
      background: rgba(0, 102, 255, 0.12);
      border: 1px solid rgba(0, 102, 255, 0.25);
      color: var(--ntt-blue-light);
    }}

    .card-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.75rem;
      line-height: 1.3;
    }}

    .card-desc {{
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Metrics & Stats */
    .stat-badge {{
      display: flex;
      flex-direction: column;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 1.25rem;
      text-align: center;
      transition: var(--transition);
    }}
    .stat-badge:hover {{
      border-color: var(--border-highlight);
      transform: translateY(-2px);
    }}
    .stat-number {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.3rem;
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
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.4rem;
      font-weight: 500;
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
      border-radius: 14px;
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
      height: 180px;
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
      transform: scale(1.04);
    }}

    .gallery-info {{
      padding: 1rem 1.2rem;
    }}

    .gallery-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.35rem;
    }}

    .gallery-desc {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.4;
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
      padding: 2rem;
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
      padding-bottom: 1rem;
    }}

    .leadership-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.2rem;
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
      padding: 1.2rem;
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
      border-radius: 16px;
      padding: 1.5rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      height: 320px;
      display: flex;
      flex-direction: column;
    }}

    .chart-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.75rem;
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
      .grid-3, .grid-4, .gallery-grid, .leadership-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Topbar -->
  <header class="topbar">
    <div class="brand-group">
      <!-- Official Logos Capsule -->
      <div class="brand-logos-capsule">
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
      <div class="slide-header" style="max-width: 1100px;">
        <div style="display: flex; gap: 0.65rem; margin-bottom: 1rem;">
          <span class="slide-tag" data-i18n="s1_badge1">PRODUCTO DESKTOP NATIVO</span>
          <span class="slide-tag" style="color: var(--success); background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.3);" data-i18n="s1_badge2">AIR-GAPPED READY</span>
          <span class="slide-tag" style="color: var(--purple); background: rgba(139, 92, 246, 0.12); border-color: rgba(139, 92, 246, 0.3);" data-i18n="s1_badge3">THREE.JS WEBGL 60FPS</span>
        </div>
        <h1 class="slide-title" style="font-size: 3.2rem; line-height: 1.15;">
          <span class="accent" data-i18n="s1_title">AXET-NeuralGraph 3D</span><br>
          <span style="font-size: 1.85rem; font-weight: 600; color: var(--text-main);" data-i18n="s1_title_accent">Plataforma Cognitiva Desktop para Reglas Técnicas & Acervos de Misión Crítica (Reef.core)</span>
        </h1>
        <p class="slide-subtitle" style="font-size: 1.15rem; margin-top: 1.25rem;" data-i18n="s1_lead">
          Ecosistema corporativo de inteligencia artificial soberana desarrollado por <strong>NTT DATA</strong> para <strong>MAPFRE</strong>. Combina un <strong>Grafo Neural Tridimensional anatómico en WebGL</strong>, <strong>RAG Local-First estricto</strong>, <strong>neuroplasticidad sintética en tiempo real</strong> y <strong>cero fuga de datos</strong> para transformar la consulta de manuales, contratos y directrices actuariales en una experiencia inmersiva e instantánea.
        </p>
      </div>

      <!-- 4 Key Metrics -->
      <div class="grid-4" style="margin-top: 2rem;">
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
      </div>

      <div style="margin-top: 2.5rem; display: flex; align-items: center; gap: 1rem;">
        <button class="btn-nav" onclick="updateSlide(2)" style="background: var(--ntt-blue); color: #fff; padding: 0.75rem 1.5rem; font-size: 0.95rem; border-color: var(--ntt-blue); border-radius: 10px;">
          <span data-i18n="s1_cta">Explorar Arquitectura y Pilares ➔</span>
        </button>
      </div>
    </section>

    <!-- SLIDE 2: DIAGNÓSTICO CRÍTICO -->
    <section class="slide-container" data-slide="2">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s2_tag">Diagnóstico Crítico</span>
        <h2 class="slide-title" data-i18n="s2_title">El Reto Estratégico: Los Riesgos de las Soluciones Web Tradicionales</h2>
        <p class="slide-subtitle" data-i18n="s2_subtitle">¿Por qué un producto desktop nativo de soberanía absoluta y no una aplicación web basada en nube pública?</p>
      </div>

      <div class="grid-3" style="margin-top: 1.5rem;">
        <div class="card" style="border-top: 3px solid var(--danger);">
          <div class="card-icon" style="background: rgba(239, 68, 68, 0.12); color: var(--danger); border-color: rgba(239, 68, 68, 0.3);">⚠️</div>
          <h3 class="card-title" data-i18n="s2_p1_title">Riesgo de Fuga de Datos y Cumplimiento</h3>
          <p class="card-desc" data-i18n="s2_p1_desc">Enviar reglas de negocio confidenciales, fórmulas técnicas de suscripción y contratos sensibles a endpoints de nubes públicas de terceros viola directrices de cumplimiento y expone la propiedad intelectual de MAPFRE a riesgos legales y filtraciones.</p>
        </div>

        <div class="card" style="border-top: 3px solid var(--warning);">
          <div class="card-icon" style="background: rgba(245, 158, 11, 0.12); color: var(--warning); border-color: rgba(245, 158, 11, 0.3);">⏱️</div>
          <h3 class="card-title" data-i18n="s2_p2_title">Latencia Crítica e Inestabilidad de Red</h3>
          <p class="card-desc" data-i18n="s2_p2_desc">Las herramientas web tradicionales dependen de llamadas REST remotas con latencias de 3 a 8 segundos. En situaciones de atención en tiempo real o auditoría de apólices, las desconexiones interrumpen el flujo analítico de los actuarios e ingenieros.</p>
        </div>

        <div class="card" style="border-top: 3px solid var(--purple);">
          <div class="card-icon" style="background: rgba(139, 92, 246, 0.12); color: var(--purple); border-color: rgba(139, 92, 246, 0.3);">🧪</div>
          <h3 class="card-title" data-i18n="s2_p3_title">Envenenamiento de Memoria (Data Poisoning)</h3>
          <p class="card-desc" data-i18n="s2_p3_desc">Los sistemas RAG web comunes sufren contaminación epistémica: cualquier archivo subido por un usuario en un chat puede indexarse de forma indiscriminada en la base vectorial corporativa, corrompiendo las respuestas para toda la compañía.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 3: LOS 6 PILARES TECNOLÓGICOS -->
    <section class="slide-container" data-slide="3">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s3_tag">Ecosistema Cognitivo</span>
        <h2 class="slide-title" data-i18n="s3_title">La Ventaja de AXET-NeuralGraph Desktop: 6 Pilares Tecnológicos</h2>
        <p class="slide-subtitle" data-i18n="s3_subtitle">Una arquitectura de ingeniería integral diseñada para velocidad, seguridad estricta y gobernanza distribuida.</p>
      </div>

      <div class="grid-3">
        <div class="card">
          <div class="card-icon">🧠</div>
          <h3 class="card-title" data-i18n="s3_c1_title">1. Grafo Neural 3D Anatómico</h3>
          <p class="card-desc" data-i18n="s3_c1_desc">Malla encefálica tridimensional en WebGL (Three.js) con 3.111 nodos y 9.472 sinapsis distribuidos según la neuroanatomía humana real (Lóbulos Temporal, Frontal, Parietal, Occipital y Cerebelo).</p>
        </div>

        <div class="card">
          <div class="card-icon">⚡</div>
          <h3 class="card-title" data-i18n="s3_c2_title">2. Neuroplasticidad en Tiempo Real</h3>
          <p class="card-desc" data-i18n="s3_c2_desc">Auto-rectificación sintética instantánea. Cuando se detecta un error de razonamiento, el sistema muta la memoria creando nodos de aprendizaje que prevalecen sobre documentaciones legadas.</p>
        </div>

        <div class="card">
          <div class="card-icon">🌐</div>
          <h3 class="card-title" data-i18n="s3_c3_title">3. Federación Git Cero Permisos</h3>
          <p class="card-desc" data-i18n="s3_c3_desc">Colaboración distribuida sin credenciales de repositorio. Cientos de usuarios comparten sinapsis vía Outbox local e Issues etiquetadas, con releases empaquetados en &lt; 2 segundos.</p>
        </div>

        <div class="card">
          <div class="card-icon">🛡️</div>
          <h3 class="card-title" data-i18n="s3_c4_title">4. RAG Local-First Estricto</h3>
          <p class="card-desc" data-i18n="s3_c4_desc">Aislamiento total en localhost (127.0.0.1). Entrega de conocimiento por snapshots cifrados (.qpack) con verificación SHA-256 y blindaje epistémico ante adjuntos efímeros.</p>
        </div>

        <div class="card">
          <div class="card-icon">📎</div>
          <h3 class="card-title" data-i18n="s3_c5_title">5. Chat Multimodal con Telemetría SSE</h3>
          <p class="card-desc" data-i18n="s3_c5_desc">Lectura nativa en memoria de PDFs corporativos, PPTs (incluyendo notas de orador) y DOCX, con visión computacional y streaming de estado en tiempo real vía Server-Sent Events.</p>
        </div>

        <div class="card">
          <div class="card-icon">⚖️</div>
          <h3 class="card-title" data-i18n="s3_c6_title">6. Matriz Regulatoria & Glosario De ➔ Para</h3>
          <p class="card-desc" data-i18n="s3_c6_desc">Módulo administrativo que armoniza órganos reguladores por país (SUSEP Brasil, DGSFP España) con thesaurus semántico para equivalencia técnica y actuarial inmediata.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 4: GRAFO NEURAL 3D -->
    <section class="slide-container" data-slide="4">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s4_tag">Cartografía Cognitiva</span>
        <h2 class="slide-title" data-i18n="s4_title">Grafo Neural 3D: Estructura Encefálica de Misión Crítica</h2>
        <p class="slide-subtitle" data-i18n="s4_subtitle">Navegación espacial interactiva a 60 FPS inspirada en la neuroanatomía del cerebro humano.</p>
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1.15fr; gap: 2rem; align-items: center;">
        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="card" style="padding: 1.25rem; border-left: 4px solid var(--ntt-blue);">
            <h4 class="card-title" style="font-size: 1.05rem;" data-i18n="s4_l1_title">Lóbulo Temporal (36% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s4_l1_desc">Memoria declarativa y semántica profunda. Alberga los contratos maestros, apólices activas, especificaciones de Reef.core y el histórico consolidado de jurisprudencia.</p>
          </div>
          <div class="card" style="padding: 1.25rem; border-left: 4px solid var(--ntt-cyan);">
            <h4 class="card-title" style="font-size: 1.05rem;" data-i18n="s4_l2_title">Lóbulo Frontal (28% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s4_l2_desc">Corteza prefrontal ejecutiva. Orquesta la toma de decisiones, reglas de suscripción (DUP), gobernanza de riesgos y razonamiento lógico-matemático de tarificación.</p>
          </div>
          <div class="card" style="padding: 1.25rem; border-left: 4px solid var(--purple);">
            <h4 class="card-title" style="font-size: 1.05rem;" data-i18n="s4_l3_title">Lóbulo Parietal (24% del Grafo)</h4>
            <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s4_l3_desc">Integración sensorial y de conectividad técnica. Mapea endpoints de API, esquemas JSON, contratos de microservicios y sincronización con sistemas centrales.</p>
          </div>
          <div class="card" style="padding: 1.25rem; border-left: 4px solid var(--success);">
            <h4 class="card-title" style="font-size: 1.05rem;" data-i18n="s4_l4_title">Lóbulo Occipital & Cerebelo (12%)</h4>
            <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s4_l4_desc">Procesamiento multimodal visual (diagramas técnicos, flujogramas de procesos) y control de telemetria motora en streaming SSE a alta tasa de refresco.</p>
          </div>
        </div>

        <!-- Interactive Preview -->
        <div class="card" style="padding: 0.5rem; overflow: hidden; cursor: pointer;" onclick="openImageModal('assets/screen_neural_graph_3d.jpg', 'Grafo Neural Tridimensional')">
          <img src="assets/screen_neural_graph_3d.jpg" alt="Grafo Neural 3D" style="width: 100%; border-radius: 12px; display: block; object-fit: cover;">
          <div style="padding: 0.75rem 1rem; font-size: 0.85rem; color: var(--ntt-cyan); font-weight: 600; text-align: center;">
            🔍 Clic para ampliar captura en alta resolución (Three.js WebGL)
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 5: RAG LOCAL-FIRST & BLINDAJE -->
    <section class="slide-container" data-slide="5">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s5_tag">Soberanía & Seguridad</span>
        <h2 class="slide-title" data-i18n="s5_title">RAG Local-First Estricto & Blindaje Epistémico</h2>
        <p class="slide-subtitle" data-i18n="s5_subtitle">Cómo AXET garantiza inmunidad total contra fugas de datos y envenenamiento de memoria.</p>
      </div>

      <div class="grid-3" style="margin-top: 1.5rem;">
        <div class="card">
          <div class="card-icon" style="background: rgba(16, 185, 129, 0.12); color: var(--success); border-color: rgba(16, 185, 129, 0.3);">🔒</div>
          <h3 class="card-title" data-i18n="s5_k1_title">Aislamiento Inviolable en 127.0.0.1</h3>
          <p class="card-desc" data-i18n="s5_k1_desc">Todo el pipeline de búsqueda semántica, cálculo de embeddings densos y orquestación de prompts se ejecuta exclusivamente en el localhost del usuario. <strong>Ningún fragmento de texto abandona la máquina de trabajo.</strong></p>
        </div>

        <div class="card">
          <div class="card-icon" style="background: rgba(0, 102, 255, 0.12); color: var(--ntt-blue-light); border-color: rgba(0, 102, 255, 0.3);">📦</div>
          <h3 class="card-title" data-i18n="s5_k2_title">Snapshots Vetoriales Compactados (.qpack)</h3>
          <p class="card-desc" data-i18n="s5_k2_desc">El conocimiento técnico de Reef.core no se distribuye como archivos de texto en disco, sino empaquetado en colecciones Qdrant binarias cifradas con hash SHA-256 verificado al inicio de la aplicación.</p>
        </div>

        <div class="card">
          <div class="card-icon" style="background: rgba(139, 92, 246, 0.12); color: var(--purple); border-color: rgba(139, 92, 246, 0.3);">🛡️</div>
          <h3 class="card-title" data-i18n="s5_k3_title">Blindaje Epistémico de Adjuntos</h3>
          <p class="card-desc" data-i18n="s5_k3_desc">Los archivos adjuntos al chat (PDFs de apólices, capturas de pantalla, planillas) tienen un ciclo de vida estrictamente efímero en RAM: <strong>tienen prohibido contaminar la memoria permanente</strong>, blindando el modelo contra data poisoning.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 6: NEUROPLASTICIDAD SINTÉTICA -->
    <section class="slide-container" data-slide="6">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s6_tag">IA con Aprendizaje Continuo</span>
        <h2 class="slide-title" data-i18n="s6_title">Neuroplasticidad Sintética: Auto-Rectificación en Tiempo Real</h2>
        <p class="slide-subtitle" data-i18n="s6_subtitle">El agente que detecta incongruencias en su propio razonamiento y muta su memoria de forma inmediata.</p>
      </div>

      <div class="grid-3" style="margin-top: 1.5rem;">
        <div class="card" style="border-left: 4px solid var(--ntt-blue);">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: var(--ntt-blue-light); margin-bottom: 0.5rem;" data-i18n="s6_s1_step">PASO 01</div>
          <h3 class="card-title" data-i18n="s6_s1_title">Detección de Divergencia</h3>
          <p class="card-desc" data-i18n="s6_s1_desc">Al interactuar con el actuario o ingeniero, el modelo contrasta la consulta con la base consolidada y detecta si una premisa técnica o regla de negocio ha quedado desfasada.</p>
        </div>

        <div class="card" style="border-left: 4px solid var(--ntt-cyan);">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: var(--ntt-cyan); margin-bottom: 0.5rem;" data-i18n="s6_s2_step">PASO 02</div>
          <h3 class="card-title" data-i18n="s6_s2_title">Mutación Topológica del Grafo</h3>
          <p class="card-desc" data-i18n="s6_s2_desc">El sistema genera de forma autónoma un nuevo nodo `APRENDIZADO_COGNITIVO` y una arista `RETIFICA_CONCEITO` con peso matemático reforzado (2.5+) apuntando al concepto corregido.</p>
        </div>

        <div class="card" style="border-left: 4px solid var(--success);">
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: var(--success); margin-bottom: 0.5rem;" data-i18n="s6_s3_step">PASO 03</div>
          <h3 class="card-title" data-i18n="s6_s3_title">Prevalencia Canónica Universal</h3>
          <p class="card-desc" data-i18n="s6_s3_desc">A partir de ese instante, cualquier consulta futura de la organización prioriza el nodo rectificado sobre la documentación histórica, eliminando el riesgo de errores reiterados.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 7: FEDERACIÓN GIT CERO PERMISOS -->
    <section class="slide-container" data-slide="7">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s7_tag">Gobernanza Distribuida</span>
        <h2 class="slide-title" data-i18n="s7_title">Federación Git Cero Permisos: Colaboración a Escala</h2>
        <p class="slide-subtitle" data-i18n="s7_subtitle">Cientos de colaboradores sincronizando mejoras de conocimiento sin requerir credenciales en el repositorio de código.</p>
      </div>

      <div class="grid-4" style="margin-top: 1.5rem;">
        <div class="card">
          <div class="card-icon">📤</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_f1_title">1. Outbox Local Desacoplado</h3>
          <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s7_f1_desc">Cada aprendizaje generado por el usuario se serializa localmente en su Outbox personal, sin exigir credenciales ni tokens de desarrollador en GitHub.</p>
        </div>

        <div class="card">
          <div class="card-icon">🏷️</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_f2_title">2. Sincronización vía Issues</h3>
          <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s7_f2_desc">El cliente desktop envía los paquetes de aprendizaje como GitHub Issues con la etiqueta `cognitive-learning`, manteniendo el código fuente blindado contra escritura.</p>
        </div>

        <div class="card">
          <div class="card-icon">👑</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_f3_title">3. Curaduría Master Admin</h3>
          <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s7_f3_desc">En el panel web administrativo, los líderes técnicos evalúan las propuestas, auditando el impacto en el grafo antes de aprobar la incorporación oficial.</p>
        </div>

        <div class="card">
          <div class="card-icon">🚀</div>
          <h3 class="card-title" style="font-size: 1.05rem;" data-i18n="s7_f4_title">4. Release Global en &lt; 2s</h3>
          <p class="card-desc" style="font-size: 0.85rem;" data-i18n="s7_f4_desc">El pipeline compila el nuevo snapshot binario y lo distribuye vía GitHub Releases. Todos los escritorios de MAPFRE se actualizan en segundo plano en instantes.</p>
        </div>
      </div>
    </section>

    <!-- SLIDE 8: GALERÍA DE PANTALLAS -->
    <section class="slide-container" data-slide="8">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s8_tag">Experiencia de Usuario</span>
        <h2 class="slide-title" data-i18n="s8_title">Galería de Pantallas Reales de la Aplicación Desktop</h2>
        <p class="slide-subtitle" data-i18n="s8_subtitle">Interfaz de alto rendimiento diseñada en Tauri v2, Next.js y Three.js para la máxima agilidad operativa.</p>
      </div>

      <div class="gallery-grid">
        <div class="gallery-card" onclick="openImageModal('assets/screen_neural_graph_3d.jpg', 'Grafo Neural 3D en WebGL')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_neural_graph_3d.jpg" alt="Grafo 3D">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img1_title">Grafo Neural 3D en WebGL</h4>
            <p class="gallery-desc" data-i18n="s8_img1_desc">Malla encefálica navegable con 3.111 nodos corticales.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_node_inspection.jpg', 'Inspección de Nodos Semánticos')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_node_inspection.jpg" alt="Inspección de Nodos">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img2_title">Inspección de Nodos Semánticos</h4>
            <p class="gallery-desc" data-i18n="s8_img2_desc">Detalle técnico, sinapsis y autoridad de Reef Academy.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_graph_immersive.jpg', 'Asistente Cognitivo Inmersivo')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_graph_immersive.jpg" alt="Asistente Inmersivo">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img3_title">Asistente Cognitivo Inmersivo</h4>
            <p class="gallery-desc" data-i18n="s8_img3_desc">Copilot integrado directamente en el espacio neural 3D.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_chat_streaming.jpg', 'Chat con Streaming SSE')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_chat_streaming.jpg" alt="Chat SSE">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img4_title">Chat con Streaming SSE</h4>
            <p class="gallery-desc" data-i18n="s8_img4_desc">Telemetría dinámica en tiempo real y soporte multimodal.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_home_dashboard.jpg', 'Dashboard Inicial')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_home_dashboard.jpg" alt="Dashboard">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img5_title">Dashboard con Okta SSO</h4>
            <p class="gallery-desc" data-i18n="s8_img5_desc">Acceso unificado con perfil corporativo y atajos rápidos.</p>
          </div>
        </div>

        <div class="gallery-card" onclick="openImageModal('assets/screen_admin_regulatory.jpg', 'Matriz Regulatoria')">
          <div class="gallery-thumb-wrap">
            <img src="assets/screen_admin_regulatory.jpg" alt="Matriz Regulatoria">
          </div>
          <div class="gallery-info">
            <h4 class="gallery-title" data-i18n="s8_img6_title">Matriz Regulatoria Jurisdiccional</h4>
            <p class="gallery-desc" data-i18n="s8_img6_desc">Gestión de equivalencias normativas De ➔ Para (SUSEP / DGSFP).</p>
          </div>
        </div>
      </div>
    </section>

    <!-- SLIDE 9: RESULTADOS Y BENCHMARKS -->
    <section class="slide-container" data-slide="9">
      <div class="slide-header">
        <span class="slide-tag" data-i18n="s9_tag">Resultados Comprobados</span>
        <h2 class="slide-title" data-i18n="s9_title">Métricas Operacionales & Benchmarks Mensurados</h2>
        <p class="slide-subtitle" data-i18n="s9_subtitle">El impacto directo de AXET-NeuralGraph 3D en tiempo, costes, exactitud y seguridad para MAPFRE.</p>
      </div>

      <div class="grid-2">
        <!-- Chart 1 -->
        <div class="chart-container-box">
          <div class="chart-title">
            <span>⏱️</span> <span data-i18n="s9_chart1_title">Tiempo Medio de Resolución de Consultas (Minutos)</span>
          </div>
          <div class="chart-canvas-wrap">
            <canvas id="chartResolutionTime"></canvas>
          </div>
        </div>

        <!-- Chart 2 -->
        <div class="chart-container-box">
          <div class="chart-title">
            <span>🎯</span> <span data-i18n="s9_chart2_title">Evolución de Acuracia & Confianza Cognitiva (%)</span>
          </div>
          <div class="chart-canvas-wrap">
            <canvas id="chartAccuracy"></canvas>
          </div>
        </div>
      </div>

      <!-- 4 Stats -->
      <div class="grid-4" style="margin-top: 1.5rem;">
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--success);" data-i18n="s9_stat1_num">-95.3%</div>
          <div class="stat-label" data-i18n="s9_stat1_lbl">Reducción en Tiempo de Búsqueda</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--ntt-cyan);" data-i18n="s9_stat2_num">99.4%</div>
          <div class="stat-label" data-i18n="s9_stat2_lbl">Acuracia Técnica Sin Alucinaciones</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--purple);" data-i18n="s9_stat3_num">-90%</div>
          <div class="stat-label" data-i18n="s9_stat3_lbl">Ahorro en Infraestructura Cloud</div>
        </div>
        <div class="stat-badge">
          <div class="stat-number" style="color: var(--mapfre-red);" data-i18n="s9_stat4_num">0 seg</div>
          <div class="stat-label" data-i18n="s9_stat4_lbl">Exposición de Datos Confidenciales</div>
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
                labels: {{ color: '#94a3b8', font: {{ family: 'Inter', size: 11 }} }}
              }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}} ${{i18nData[currentLang].chart_time_unit}}`
                }}
              }}
            }},
            scales: {{
              x: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }},
              y: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }},
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
                borderWidth: 2.5,
                tension: 0.35,
                fill: true,
                pointRadius: 4,
                pointBackgroundColor: '#10b981'
              }},
              {{
                label: i18nData[currentLang].chart_acc_leg_err,
                data: [17.5, 13.0, 8.5, 3.8, 1.2, 0.6],
                borderColor: '#ef4444',
                backgroundColor: 'rgba(239, 68, 68, 0.05)',
                borderWidth: 2,
                borderDash: [5, 5],
                tension: 0.35,
                fill: false,
                pointRadius: 3,
                pointBackgroundColor: '#ef4444'
              }}
            ]
          }},
          options: {{
            responsive: true,
            maintainAspectRatio: false,
            plugins: {{
              legend: {{
                labels: {{ color: '#94a3b8', font: {{ family: 'Inter', size: 11 }} }}
              }},
              tooltip: {{
                callbacks: {{
                  label: (ctx) => `${{ctx.dataset.label}}: ${{ctx.raw}}%`
                }}
              }}
            }},
            scales: {{
              x: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }},
                grid: {{ color: 'rgba(255, 255, 255, 0.05)' }}
              }},
              y: {{
                ticks: {{ color: '#94a3b8', font: {{ size: 10 }} }},
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
    "/Users/gcostabe/Desktop/AVALIACAO Q1 Q2 MAPPS/Apresentacao_Executiva_AXET_REEF.html",
    "/Users/gcostabe/dev/RAG-LOCAL-REEF/Apresentacao_Executiva_AXET_REEF.html"
]

for t in targets:
    with open(t, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"SUCCESS: Generated {t} ({len(html_template)} bytes)")

