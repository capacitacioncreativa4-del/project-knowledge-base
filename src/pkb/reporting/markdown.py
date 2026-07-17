from pkb.knowledge.catalog import KnowledgeCatalog

class MarkdownInventoryReport:
    """Responsable de formatear el inventario acumulado del catálogo en un reporte estructurado Markdown."""
    
    @staticmethod
    def generate(catalog: KnowledgeCatalog) -> str:
        """Construye un informe en texto plano con el resumen cuantitativo del repositorio."""
        lineas = [
            "# Inventario Automático de Objetos de Conocimiento",
            "",
            "Este informe resume de forma estadística la composición y distribución por tipos y dominios",
            "de los artefactos almacenados en la plataforma.",
            "",
            "## 📦 Resumen por Tipo de Objeto",
            "",
            "| Tipo de Objeto | Cantidad |",
            "| :--- | :---: |"
        ]
        
        # Agregamos filas ordenadas por frecuencia descendente
        por_tipo = catalog.by_type()
        for tipo, cantidad in por_tipo.most_common():
            lineas.append(f"| {tipo} | {cantidad} |")
            
        lineas.extend([
            "",
            "## 🌐 Resumen por Dominio",
            "",
            "| Dominio | Cantidad |",
            "| :--- | :---: |"
        ])
        
        por_dominio = catalog.by_domain()
        for dominio, cantidad in por_dominio.most_common():
            lineas.append(f"| {dominio} | {cantidad} |")
            
        return "\n".join(lineas)