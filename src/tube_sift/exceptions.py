from __future__ import annotations


class TubeSiftError(Exception):
    """Base exception for TubeSift."""


class ConfigError(TubeSiftError):
    """Invalid or inconsistent configuration."""


class PreflightError(TubeSiftError):
    """Preflight checks failed."""

    def __init__(self, results: list[dict]) -> None:
        self.results = results
        failed = [r for r in results if not r.get("OK")]
        names = ", ".join(r.get("NAME", "?") for r in failed) or "unknown"
        super().__init__(f"Preflight failed: {names}")


class CollectionError(TubeSiftError):
    """Error during comment/transcript collection."""


class EnrichmentError(TubeSiftError):
    """Error during enrichment pipeline."""
