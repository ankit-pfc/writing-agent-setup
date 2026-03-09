"""
LLM Client Service - Wrapper for Anthropic Claude API
Provides a unified interface for all agent LLM calls.
"""
import os
from typing import Optional, List, Dict, Any
from app.core.config import settings


class LLMClient:
    """
    Wrapper for Anthropic Claude API with configurable model settings.
    Falls back to mock mode if API key is not configured.
    """
    
    def __init__(
        self,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ):
        self.model = model or settings.LLM_MODEL
        self.max_tokens = max_tokens or settings.LLM_MAX_TOKENS
        self.temperature = temperature or settings.LLM_TEMPERATURE
        self.api_key = settings.ANTHROPIC_API_KEY
        self._client = None
        
    @property
    def client(self):
        """Lazy-load the Anthropic client."""
        if self._client is None:
            if self.api_key:
                try:
                    import anthropic
                    self._client = anthropic.Anthropic(api_key=self.api_key)
                except ImportError:
                    print("[LLMClient] Warning: anthropic package not installed. Using mock mode.")
            else:
                print("[LLMClient] Warning: ANTHROPIC_API_KEY not set. Using mock mode.")
        return self._client
    
    def generate(
        self,
        system_prompt: str,
        user_message: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None
    ) -> str:
        """
        Generate content using the LLM.
        
        Args:
            system_prompt: The system prompt defining behavior
            user_message: The user's request/content
            max_tokens: Override default max tokens
            temperature: Override default temperature
            
        Returns:
            Generated text content
        """
        max_tokens = max_tokens or self.max_tokens
        temperature = temperature or self.temperature
        
        if self.client:
            # Real API call
            try:
                message = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    system=system_prompt,
                    messages=[
                        {"role": "user", "content": user_message}
                    ]
                )
                return message.content[0].text
            except Exception as e:
                print(f"[LLMClient] Error calling API: {e}")
                return self._mock_generate(system_prompt, user_message)
        else:
            # Mock mode for development
            return self._mock_generate(system_prompt, user_message)
    
    def _mock_generate(self, system_prompt: str, user_message: str) -> str:
        """
        Mock generation for development/testing without API key.
        """
        return (
            f"[MOCK OUTPUT - Set ANTHROPIC_API_KEY for real generation]\n\n"
            f"System prompt length: {len(system_prompt)} chars\n"
            f"User message: {user_message[:200]}{'...' if len(user_message) > 200 else ''}\n\n"
            f"This is placeholder content. Configure ANTHROPIC_API_KEY in .env "
            f"to enable real Claude API calls."
        )
    
    def generate_with_context(
        self,
        system_prompt: str,
        user_message: str,
        context: Optional[Dict[str, Any]] = None,
        examples: Optional[List[Dict[str, str]]] = None
    ) -> str:
        """
        Generate with additional context and few-shot examples.
        
        Args:
            system_prompt: The system prompt
            user_message: The user's request
            context: Additional context to inject
            examples: List of {"input": ..., "output": ...} examples
            
        Returns:
            Generated text content
        """
        enhanced_message = user_message
        
        if context:
            context_str = "\n\n".join(
                f"## {k}\n{v}" for k, v in context.items()
            )
            enhanced_message = f"{context_str}\n\n---\n\n{user_message}"
        
        if examples:
            examples_str = "\n\n".join(
                f"Example {i+1}:\nInput: {ex['input']}\nOutput: {ex['output']}"
                for i, ex in enumerate(examples)
            )
            enhanced_message = f"{examples_str}\n\n---\n\n{enhanced_message}"
        
        return self.generate(system_prompt, enhanced_message)


# Singleton instance for convenience
_default_client = None

def get_llm_client() -> LLMClient:
    """Get the default LLM client instance."""
    global _default_client
    if _default_client is None:
        _default_client = LLMClient()
    return _default_client