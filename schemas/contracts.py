from dataclasses import dataclass,field
@dataclass
class DocumentationContext:
    documents:list=field(default_factory=list)
    requirements:list=field(default_factory=list)
    evidence_gaps:list=field(default_factory=list)
