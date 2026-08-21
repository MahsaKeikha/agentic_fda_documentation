def gaps(required:list[str],present:list[str])->list[str]:return [x for x in required if x not in present]
