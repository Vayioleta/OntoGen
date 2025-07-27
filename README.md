# 🧠 OntoTransformer

**OntoTransformer** es un modelo de inteligencia artificial diseñado para interpretar descripciones de productos y convertirlas en representaciones estructuradas basadas en el modelo OntoIMM (Ontology-based Intelligent Master Model).

Utiliza redes neuronales del tipo Transformer para comprender el lenguaje natural y extraer automáticamente:

- 📌 Qué es el producto (*Know-What*)
- 🎯 Para qué sirve (*Know-Why*)
- 🛠️ Cómo se usa o ensambla (*Know-How*)

### 💡 Casos de uso
- Clasificación semántica avanzada en e-commerce
- Generación automatizada de ontologías OWL/JSON-LD
- Razonamiento de producto en sistemas expertos
- Enriquecimiento de SKOS o taxonomías jerárquicas

### 🛠️ Tecnologías sugeridas
- `transformers` de HuggingFace
- `spaCy` para NER y parsing
- `rdflib` o `OWLready2` para exportar a ontologías
- Entrenamiento supervisado con anotaciones tipo OntoIMM
