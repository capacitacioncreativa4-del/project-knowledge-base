from pkb.repository.scanner import RepositoryScanner
from pkb.metadata.parser import MetadataParser
from pkb.knowledge.registry import KnowledgeRegistry

class KnowledgeLoader:
    """Orquestador encargado de escanear, parsear y cargar el repositorio completo en el SSoT."""
    
    @staticmethod
    def load_repository(ruta_raiz: str = ".") -> KnowledgeRegistry:
        """Escanéa el directorio, convierte la metadata y puebla un registro centralizado."""
        registry = KnowledgeRegistry()
        
        # 1. Localizar todos los archivos Markdown
        archivos = RepositoryScanner.markdown_files(ruta_raiz)
        
        # 2. Procesar y registrar cada archivo individualmente
        for archivo in archivos:
            try:
                # El parser lee el archivo y devuelve un KnowledgeObject ya construido
                knowledge_object, _ = MetadataParser.parse_file(str(archivo))
                
                if knowledge_object:
                    # NORMALIZACIÓN CRUCIAL: Forzamos mayúsculas y removemos espacios en las propiedades de análisis
                    if hasattr(knowledge_object, "object_type") and knowledge_object.object_type:
                        knowledge_object.object_type = str(knowledge_object.object_type).upper().strip()
                        
                    if hasattr(knowledge_object, "domain") and knowledge_object.domain:
                        knowledge_object.domain = str(knowledge_object.domain).upper().strip()
                    
                    # Registrar de forma segura en la Fuente Única de Verdad (SSoT)
                    registry.add(knowledge_object)
                
            except Exception:
                # Omitimos archivos que no tengan front-matter estructural válido
                continue
                
        return registry