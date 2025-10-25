"""
Tai Chi AI Rehabilitation Program
AI-powered workout program for injury rehabilitation
"""

__version__ = "1.0.0"
__author__ = "AI Rehabilitation Team"

from .main import TaiChiProgram
from .core.ai_agents import TaiChiCoachAgent, ProgressTrackerAgent, SafetyMonitorAgent

__all__ = [
    "TaiChiProgram",
    "TaiChiCoachAgent", 
    "ProgressTrackerAgent",
    "SafetyMonitorAgent"
]
