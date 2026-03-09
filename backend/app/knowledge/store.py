import json
import os
import re
from typing import List, Dict, Any, Optional

class KnowledgeStore:
    """
    Loads deterministic JSON data at startup and provides rapid query methods for agents.
    Enforces Phase 1 hard SEO + voice rules.
    """
    def __init__(self, data_dir: str = "../knowledge/parsed"):
        self.data_dir = data_dir
        self.exclusions: List[re.Pattern] = []
        self.content_rules: Dict[str, Any] = {}
        self.link_map: Dict[str, str] = {}
        
        self.load_all()

    def load_all(self):
        """Loads all JSON files into memory (<2MB for fast access)."""
        if not os.path.exists(self.data_dir):
            return

        # Load Exclusions (precompiled Regex)
        exc_file = os.path.join(self.data_dir, "exclusions.json")
        if os.path.exists(exc_file):
            with open(exc_file, "r") as f:
                data = json.load(f)
                patterns = data.get("regex_patterns", [])
                self.exclusions = [re.compile(p) for p in patterns]

        # Load Content Rules per page type
        cr_file = os.path.join(self.data_dir, "content_rules.json")
        if os.path.exists(cr_file):
            with open(cr_file, "r") as f:
                rules_list = json.load(f)
                for r in rules_list:
                    self.content_rules[r.get("page_type")] = r
                    
        # Load Internal Linking Map
        lm_file = os.path.join(self.data_dir, "link_map.json")
        if os.path.exists(lm_file):
            with open(lm_file, "r") as f:
                map_list = json.load(f)
                for item in map_list:
                    self.link_map[item.get("concept")] = item.get("canonical_url")

    def get_exclusion_patterns(self) -> List[re.Pattern]:
        """Returns compiled regex array for Editor's fail-closed scanning"""
        return self.exclusions
        
    def get_content_rules(self, page_type: str) -> Optional[Dict[str, Any]]:
        """Returns min words and required sections for a specific page type."""
        return self.content_rules.get(page_type)

    def get_internal_link_targets(self, text: str) -> List[Dict[str, str]]:
        """Scans arbitrary text for concepts from the JSON map and returns their intended URLs."""
        found = []
        for concept, url in self.link_map.items():
            if re.search(rf"\b{re.escape(concept)}\b", text, re.IGNORECASE):
                found.append({"concept": concept, "url": url})
        return found
