import pytest
import pandas as pd
from datetime import datetime

from src.tai_chi_ai.core.ai_agents import TaiChiCoachAgent, ProgressTrackerAgent, SafetyMonitorAgent
from src.tai_chi_ai.data.models import BodyPart, InjurySeverity, WorkoutPhase


class TestTaiChiCoachAgent:
    def test_agent_initialization(self):
        agent = TaiChiCoachAgent()
        assert agent.name == "TaiChi Coach Pro"
        assert agent.specialty == "Exercise prescription and modification"
        assert "tai_chi_principles" in agent.knowledge_base
    
    def test_injury_impact_analysis(self):
        agent = TaiChiCoachAgent()
        injuries = {
            BodyPart.LEFT_SHOULDER: InjurySeverity.MODERATE,
            BodyPart.LOWER_BACK: InjurySeverity.MILD
        }
        
        impact = agent.analyze_injury_impact(injuries)
        
        assert "restrictions" in impact
        assert "modifications" in impact
        assert "focus_areas" in impact
        assert len(impact["restrictions"]) > 0
    
    def test_workout_generation(self):
        agent = TaiChiCoachAgent()
        injuries = {BodyPart.LEFT_SHOULDER: InjurySeverity.MILD}
        impact = agent.analyze_injury_impact(injuries)
        
        workout = agent.generate_workout_plan(
            WorkoutPhase.FOUNDATION, 
            impact, 
            week=1
        )
        
        assert workout["phase"] == WorkoutPhase.FOUNDATION
        assert workout["week"] == 1
        assert "exercises" in workout
        assert len(workout["exercises"]) > 0


class TestProgressTrackerAgent:
    def test_session_recording(self):
        tracker = ProgressTrackerAgent()
        session_data = {
            "phase": WorkoutPhase.FOUNDATION,
            "week": 1,
            "duration_minutes": 15,
            "pain_level": 2,
            "fatigue_level": 3,
            "completion_percentage": 90
        }
        
        tracker.record_session(session_data)
        assert len(tracker.progress_data) == 1
    
    def test_trend_analysis(self):
        tracker = ProgressTrackerAgent()
        
        # Add some test data
        for i in range(5):
            session_data = {
                "phase": WorkoutPhase.FOUNDATION,
                "week": i + 1,
                "duration_minutes": 10 + i * 2,
                "pain_level": max(0, 3 - i),
                "fatigue_level": 2,
                "completion_percentage": 85 + i * 3
            }
            tracker.record_session(session_data)
        
        analysis = tracker.analyze_trends()
        
        assert "performance_metrics" in analysis
        assert "trends" in analysis
        assert "recommendations" in analysis
        assert isinstance(analysis["recommendations"], list)


class TestSafetyMonitorAgent:
    def test_safety_assessment(self):
        monitor = SafetyMonitorAgent()
        session_data = {
            "pain_level": 3,
            "fatigue_level": 4,
            "completion_percentage": 95
        }
        
        assessment = monitor.assess_session_safety(session_data)
        
        assert "safety_level" in assessment
        assert "immediate_actions" in assessment
        assert assessment["clearance_for_next_session"] is True
    
    def test_high_pain_safety_check(self):
        monitor = SafetyMonitorAgent()
        session_data = {
            "pain_level": 8,  # High pain level
            "fatigue_level": 3,
            "completion_percentage": 60
        }
        
        assessment = monitor.assess_session_safety(session_data)
        
        assert assessment["safety_level"] == "red"
        assert assessment["clearance_for_next_session"] is False


if __name__ == "__main__":
    pytest.main([__file__])
