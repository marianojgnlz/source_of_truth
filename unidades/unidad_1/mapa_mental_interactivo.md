<script src="https://d3js.org/d3.v7.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
<style>
    .mindmap-body {
        font-family: 'Inter', sans-serif;
    }
    .node {
        cursor: pointer;
        transition: transform 0.2s ease-in-out;
    }
    .node:hover {
        transform: scale(1.1);
    }
    .link {
        stroke-opacity: 0.6;
    }
    text {
        pointer-events: none;
        text-shadow: 0 1px 0 #fff, 1px 0 0 #fff, 0 -1px 0 #fff, -1px 0 0 #fff;
        font-weight: 500;
    }
    #info-panel {
        transition: opacity 0.3s ease-in-out;
    }
    #container {
        height: 85vh;
    }
</style>

<div class="mindmap-body bg-gray-50 text-gray-800">
    <div class="relative w-full h-full" id="container">
        <!-- Título y cabecera -->
        <div class="absolute top-0 left-0 w-full p-4 md:p-6 bg-white/80 backdrop-blur-sm z-10">
            <h1 class="text-2xl md:text-3xl font-bold text-center text-blue-800">Mapa Mental: Unidad 1</h1>
            <p class="text-center text-gray-600 mt-1">Una visión integrada de la Estrategia de SI/TI</p>
        </div>

        <!-- Contenedor para el mapa mental -->
        <svg id="mindmap" class="w-full h-full"></svg>

        <!-- Panel de información -->
        <div id="info-panel" class="absolute top-24 right-6 w-72 bg-white p-4 rounded-xl shadow-lg border border-gray-200 opacity-0 pointer-events-none">
            <h3 id="info-title" class="text-lg font-bold text-blue-700 mb-2"></h3>
            <p id="info-description" class="text-sm text-gray-600"></p>
        </div>
        
        <!-- Controles de Zoom -->
        <div class="absolute bottom-6 right-6 flex flex-col space-y-2 z-10">
            <button id="zoom-in" class="w-10 h-10 bg-white rounded-full shadow-md flex items-center justify-center text-blue-600 hover:bg-blue-50 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
            </button>
            <button id="zoom-out" class="w-10 h-10 bg-white rounded-full shadow-md flex items-center justify-center text-blue-600 hover:bg-blue-50 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4" /></svg>
            </button>
             <button id="reset-zoom" class="w-10 h-10 bg-white rounded-full shadow-md flex items-center justify-center text-blue-600 hover:bg-blue-50 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h5M20 20v-5h-5M4 20l16-16" /></svg>
            </button>
        </div>

    </div>

    <script>
        // --- DATA ---
        // Definición de los nodos (conceptos) y sus relaciones (links)
        const nodes = [
            // Nivel 0: Centro
            { id: "Organización", level: 0, description: "Unidad social, sistema abierto y socio-técnico que busca objetivos específicos." },

            // Nivel 1: Conceptos base
            { id: "Sistema Abierto", level: 1, description: "Interactúa con su entorno: entradas, procesamiento, salidas y retroalimentación." },
            { id: "Sistema Socio-Técnico", level: 1, description: "Compuesto por un sistema técnico (tecnología) y uno social (personas), coordinados por un sistema gerencial." },
            { id: "Administración (PODC)", level: 1, description: "Proceso de Planificar, Organizar, Dirigir y Controlar para lograr objetivos." },
            { id: "Estrategia Empresarial", level: 1, description: "Plan de acción a largo plazo que guía a la organización." },
            { id: "Eficiencia y Eficacia", level: 1, description: "Eficiencia: Uso racional de recursos. Eficacia: Logro de resultados." },

            // Nivel 2: Derivados de Estrategia
            { id: "Alineamiento Estratégico", level: 2, description: "Proceso para asegurar que SI/TI contribuyan a la estrategia del negocio." },
            { id: "Cadena de Valor", level: 2, description: "Modelo que distingue actividades que crean valor para el cliente." },
            
            // Nivel 3: Estrategias SI/TI y Plan
            { id: "Estrategia SI (Demanda)", level: 3, description: "Define QUÉ información y sistemas se necesitan para cumplir la estrategia." },
            { id: "Estrategia TI (Oferta)", level: 3, description: "Define CÓMO se proveerán las soluciones tecnológicas a la demanda de SI." },
            { id: "Plan de SI/TI", level: 3, description: "Documento formal que traduce la estrategia en acciones y proyectos concretos." },
            { id: "Actividades de Soporte", level: 3, description: "Actividades que apoyan a las primarias, como la infraestructura (donde reside el SI)." },
            { id: "Actividades de Línea", level: 3, description: "Actividades directas en la creación del producto/servicio." },

            // Nivel 4: Componentes del Plan y Gestión
            { id: "Fases del Plan", level: 4, description: "Pasos: Compromiso, Diagnóstico (¿Dónde estoy?), Diseño (¿A dónde voy?), Programación." },
            { id: "Inversión en SI/TI", level: 4, description: "Análisis de costos y beneficios para asignar recursos a proyectos de SI/TI." },
            { id: "Management Recursos SI", level: 4, description: "Gestión del área de sistemas (rol, ubicación y organización)." },
            
            // Nivel 5: Desglose de Inversión y Management
            { id: "Cartera de Aplicaciones", level: 5, description: "Clasifica aplicaciones: Estratégicas, Clave Op., Alto Potencial, Apoyo." },
            { id: "Costos y Beneficios", level: 5, description: "Análisis de elementos tangibles e intangibles para justificar la inversión." },
            { id: "Tipos de Inversión", level: 5, description: "Clasificación por impacto (Operacional, Estratégico) o necesidad (Umbral, Infraestructura)." },
            { id: "Rol del Área SI", level: 5, description: "Define la función del área de sistemas (de proveedor a socio estratégico)." },
            { id: "Ubicación (Modelo Decisional)", level: 5, description: "Decide dónde se toman las decisiones (Centralizada, Descentralizada, Delegada)." },
            { id: "Organización (Modelo Org.)", level: 5, description: "Estructura interna del área de sistemas (Tradicional, Funcional, etc.)." },

            // Nivel 6: Detalle de Cartera
            { id: "Estrategias de Gestión", level: 6, description: "Enfoques para gestionar cada cuadrante de la cartera de aplicaciones." }
        ];

        const links = [
            { source: "Organización", target: "Sistema Abierto" },
            { source: "Organización", target: "Sistema Socio-Técnico" },
            { source: "Organización", target: "Administración (PODC)" },
            { source: "Organización", target: "Estrategia Empresarial" },
            { source: "Organización", target: "Eficiencia y Eficacia" },
            { source: "Estrategia Empresarial", target: "Alineamiento Estratégico" },
            { source: "Estrategia Empresarial", target: "Cadena de Valor" },
            { source: "Cadena de Valor", target: "Actividades de Soporte" },
            { source: "Cadena de Valor", target: "Actividades de Línea" },
            { source: "Actividades de Soporte", target: "Estrategia SI (Demanda)" },
            { source: "Alineamiento Estratégico", target: "Estrategia SI (Demanda)" },
            { source: "Alineamiento Estratégico", target: "Estrategia TI (Oferta)" },
            { source: "Estrategia SI (Demanda)", target: "Estrategia TI (Oferta)" },
            { source: "Alineamiento Estratégico", target: "Plan de SI/TI" },
            { source: "Plan de SI/TI", target: "Fases del Plan" },
            { source: "Plan de SI/TI", target: "Inversión en SI/TI" },
            { source: "Plan de SI/TI", target: "Management Recursos SI" },
            { source: "Inversión en SI/TI", target: "Cartera de Aplicaciones" },
            { source: "Inversión en SI/TI", target: "Costos y Beneficios" },
            { source: "Inversión en SI/TI", target: "Tipos de Inversión" },
            { source: "Management Recursos SI", target: "Rol del Área SI" },
            { source: "Management Recursos SI", target: "Ubicación (Modelo Decisional)" },
            { source: "Management Recursos SI", target: "Organización (Modelo Org.)" },
            { source: "Cartera de Aplicaciones", target: "Estrategias de Gestión" }
        ];

        // --- D3.js IMPLEMENTATION ---
        const container = document.getElementById('container');
        const width = container.clientWidth;
        const height = container.clientHeight;

        const svg = d3.select("#mindmap")
            .attr("viewBox", [0, 0, width, height]);

        const g = svg.append("g");

        const zoom = d3.zoom()
            .scaleExtent([0.2, 5])
            .on("zoom", (event) => {
                g.attr("transform", event.transform);
            });

        svg.call(zoom);
        
        function resetView() {
            const transform = d3.zoomIdentity.translate(width / 2, height / 2).scale(0.8);
            svg.transition().duration(750).call(zoom.transform, transform);
        }

        d3.select("#zoom-in").on("click", () => svg.transition().call(zoom.scaleBy, 1.2));
        d3.select("#zoom-out").on("click", () => svg.transition().call(zoom.scaleBy, 0.8));
        d3.select("#reset-zoom").on("click", resetView);

        const colorScale = d3.scaleOrdinal(d3.schemeCategory10)
            .domain(d3.map(nodes, d => d.level).keys());

        const simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id).distance(d => (d.source.level + d.target.level) * 30 + 60).strength(0.9))
            .force("charge", d3.forceManyBody().strength(-400))
            .force("center", d3.forceCenter(width / 2, height / 2).strength(0.4))
            .force("collide", d3.forceCollide().radius(d => 45 - d.level * 4).strength(0.9));

        const link = g.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("class", "link")
            .attr("stroke", "#999");

        const node = g.append("g")
            .attr("class", "nodes")
            .selectAll("g")
            .data(nodes)
            .enter().append("g")
            .attr("class", "node");

        // Add a larger, transparent circle to act as a reliable hover target
        node.append("circle")
            .attr("r", 45) // A generous radius for the hit area
            .style("fill", "transparent");

        // The visible circle
        node.append("circle")
            .attr("r", d => 40 - d.level * 4)
            .attr("fill", d => colorScale(d.level))
            .attr("stroke", "#fff")
            .attr("stroke-width", 2);

        const labels = node.append("text")
            .selectAll("tspan")
            .data(d => d.id.split(" "))
            .join("tspan")
            .attr("x", 0)
            .attr("y", (d, i, nodes) => `${i - (nodes.length - 1) * 0.5}em`)
            .attr("text-anchor", "middle")
            .text(d => d)
            .attr("font-size", d => `11px`);

        const infoPanel = d3.select("#info-panel");
        const infoTitle = d3.select("#info-title");
        const infoDescription = d3.select("#info-description");

        node.on("mouseover", function(event, d) {
            infoTitle.text(d.id);
            infoDescription.text(d.description);
            infoPanel.style("opacity", 1).style("pointer-events", "auto");
        });

        node.on("mouseout", function() {
            infoPanel.style("opacity", 0).style("pointer-events", "none");
        });

        simulation.on("tick", () => {
            link
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node
                .attr("transform", d => `translate(${d.x},${d.y})`);
        });
        
        window.onload = () => {
            setTimeout(resetView, 150);
        };

        window.onresize = () => {
            const newWidth = container.clientWidth;
            const newHeight = container.clientHeight;
            svg.attr("viewBox", [0, 0, newWidth, newHeight]);
            simulation.force("center", d3.forceCenter(newWidth / 2, newHeight / 2));
            simulation.alpha(0.3).restart();
        }

    </script>
</div> 