import json
import os
import re

class KnowledgeParser:
    """
    Parses Markdown and unstructured JSON files into deterministic structured JSON.
    This simulates Phase 1 mapping of rules, clusters, and SEO boundaries.
    """
    def __init__(self, raw_source_dir: str, parsed_dest_dir: str):
        self.raw_source_dir = raw_source_dir
        self.parsed_dest_dir = parsed_dest_dir
        
        if not os.path.exists(parsed_dest_dir):
            os.makedirs(parsed_dest_dir)

    def parse_exclusions(self, md_filepath: str):
        """
        Parses `exclusions.md` into regex patterns for safety checking.
        Expects lines like: `- ZERO medical claims` or specific words to avoid.
        In a real app, this uses advanced NLP or regex parsing. Here we mock it based on SOUL.md.
        """
        patterns = [
            r"\b(delve|leverage|utilize|robust|seamless|transformative|cutting-edge)\b",
            r"(?i)\bin today's\b",
            r"(?i)\bin the ever-evolving\b",
            r"(?i)\blet's delve\b",
            r"(?i)\bin conclusion\b",
            r"—" # em dashes
        ]
        
        dest_file = os.path.join(self.parsed_dest_dir, "exclusions.json")
        with open(dest_file, "w") as f:
            json.dump({"regex_patterns": patterns}, f, indent=4)
        print(f"Parsed exclusions -> {dest_file}")

    def generate_dummy_knowledge(self):
        """
        Since we might not have all the initial text files populated in Phase 1 setup,
        this utility seeds the structured JSON directly into the destination directory based
        on the blueprint requirements.
        """
        # Save content rules
        content_rules = [
            {"page_type": "blog_post", "min_words": 1500, "required_sections": ["H1", "Introduction", "H2s", "FAQ", "Conclusion"]},
            {"page_type": "glossary_term", "min_words": 800, "required_sections": ["H1", "Quick Summary", "Detailed Meaning", "FAQ", "Related Terms"]}
        ]
        with open(os.path.join(self.parsed_dest_dir, "content_rules.json"), "w") as f:
            json.dump(content_rules, f, indent=4)
            
        # Save link map for internal linking
        link_map = [
            {"concept": "Advaita Vedanta", "canonical_url": "/advaita-vedanta-guide"},
            {"concept": "Krishna", "canonical_url": "/krishna-teachings"}
        ]
        with open(os.path.join(self.parsed_dest_dir, "link_map.json"), "w") as f:
            json.dump(link_map, f, indent=4)
            
        print("Generated initial dummy knowledge store JSON.")

if __name__ == "__main__":
    parser = KnowledgeParser(
        raw_source_dir="../../knowledge/raw",
        parsed_dest_dir="../../knowledge/parsed"
    )
    parser.generate_dummy_knowledge()
    parser.parse_exclusions("../../knowledge/raw/exclusions.md")
