from enum import Enum
from typing import Dict, List, Optional, Any
import pandas as pd
from datetime import datetime
from ..data.models import BodyPart, InjurySeverity, WorkoutPhase


class AIAgent:
    """Base class for all AI agents in the Tai Chi system"""
    
    def __init__(self, name: str, specialty: str):
        self.name = name
        self.specialty = specialty
        self.knowledge_base = self._initialize_knowledge_base()
    
    def _initialize_knowledge_base(self) -> Dict[str, Any]:
        return {
            "tai_chi_principles": ["relaxation", "rooting", "alignment", "flow", "breath control"],
            "injury_modifications": self._load_injury_modifications(),
            "progression_rules": self._load_progression_rules()
        }
    
    def _load_injury_modifications(self) -> Dict[BodyPart, Dict]:
        return {
            BodyPart.LEFT_SHOULDER: {
                "avoid": ["high arm raises", "shoulder rotations", "weight bearing on arms"],
                "modify": ["keep arms below shoulder height", "reduce range of motion", "focus on lower body"],
                "compensatory": ["leg strength", "core stability", "breathing techniques"]
            },
            BodyPart.RIGHT_SHOULDER: {
                "avoid": ["high arm raises", "shoulder rotations", "weight bearing on arms"],
                "modify": ["keep arms below shoulder height", "reduce range of motion", "focus on lower body"],
                "compensatory": ["leg strength", "core stability", "breathing techniques"]
            },
            BodyPart.LEFT_CALF: {
                "avoid": ["deep stances", "jumping", "prolonged standing"],
                "modify": ["shorter stances", "chair support", "reduced duration"],
                "compensatory": ["upper body flow", "seated practice", "breathing focus"]
            },
            BodyPart.LOWER_BACK: {
                "avoid": ["forward bends", "twisting", "arching"],
                "modify": ["maintain neutral spine", "bend knees", "use support"],
                "compensatory": ["gentle core engagement", "postural awareness", "gradual progression"]
            }
        }
    
    def _load_progression_rules(self) -> Dict[str, Any]:
        return {
            "phase_duration_weeks": {
                WorkoutPhase.FOUNDATION: 12,
                WorkoutPhase.BUILDING: 12,
                WorkoutPhase.INTEGRATION: 12,
                WorkoutPhase.MASTERY: 16
            },
            "intensity_parameters": {
                "duration_increment": [5, 10, 15, 20, 25, 30, 35, 40, 45],
                "complexity_level": ["basic", "simple", "moderate", "advanced", "master"],
                "frequency_multiplier": [1, 2, 3, 4, 5]
            }
        }


class TaiChiCoachAgent(AIAgent):
    """AI agent specialized in Tai Chi exercise prescription"""
    
    def __init__(self):
        super().__init__("TaiChi Coach Pro", "Exercise prescription and modification")
        self.exercise_library = self._load_exercise_library()
    
    def _load_exercise_library(self) -> Dict[str, Dict]:
        return {
            "breathing": {
                "abdominal_breathing": {
                    "difficulty": 1, 
                    "impact": "low",
                    "description": "Focus on diaphragmatic breathing",
                    "benefits": ["relaxation", "oxygenation", "stress reduction"]
                },
                "reverse_breathing": {
                    "difficulty": 2, 
                    "impact": "low",
                    "description": "Advanced breathing technique with abdominal control",
                    "benefits": ["energy flow", "core engagement", "mental focus"]
                }
            },
            "warmup": {
                "joint_rotations": {
                    "difficulty": 1, 
                    "impact": "low",
                    "description": "Gentle rotation of all major joints",
                    "benefits": ["mobility", "circulation", "preparation"]
                },
                "gentle_stretching": {
                    "difficulty": 1, 
                    "impact": "low", 
                    "description": "Light stretching for major muscle groups",
                    "benefits": ["flexibility", "injury prevention", "body awareness"]
                }
            },
            "qigong": {
                "standing_meditation": {
                    "difficulty": 1, 
                    "impact": "low",
                    "description": "Static standing practice with focus on alignment",
                    "benefits": ["rooting", "posture", "mental calm"]
                },
                "cloud_hands": {
                    "difficulty": 2, 
                    "impact": "medium",
                    "description": "Flowing arm movements with weight shifting",
                    "benefits": ["coordination", "flow", "balance"]
                }
            },
            "forms": {
                "commencement": {
                    "difficulty": 1, 
                    "impact": "low",
                    "description": "Opening movement of Tai Chi forms",
                    "benefits": ["centering", "beginning awareness", "energy gathering"]
                },
                "ward_off": {
                    "difficulty": 2, 
                    "impact": "medium",
                    "description": "Defensive posture with circular energy",
                    "benefits": ["structure", "warding energy", "upper-lower integration"]
                }
            }
        }
    
    def analyze_injury_impact(self, injuries: Dict[BodyPart, InjurySeverity]) -> Dict[str, Any]:
        """Comprehensive analysis of injury impacts on Tai Chi practice"""
        impact_assessment = {
            "restrictions": [],
            "modifications": [],
            "focus_areas": [],
            "compensatory_strategies": [],
            "risk_factors": [],
            "rehabilitation_focus": []
        }
        
        for body_part, severity in injuries.items():
            modifications = self.knowledge_base["injury_modifications"][body_part]
            
            # Add severity-based modifications
            impact_assessment["restrictions"].extend(
                f"{restriction} ({severity.value})" 
                for restriction in modifications["avoid"]
            )
            impact_assessment["modifications"].extend(modifications["modify"])
            impact_assessment["compensatory_strategies"].extend(modifications["compensatory"])
            
            # Body part specific focus areas
            if body_part in [BodyPart.LEFT_SHOULDER, BodyPart.RIGHT_SHOULDER]:
                impact_assessment["focus_areas"].extend([
                    "lower body stability and rooting",
                    "deep diaphragmatic breathing",
                    "mental visualization of arm movements"
                ])
                impact_assessment["rehabilitation_focus"].append("gradual shoulder mobility restoration")
                
            elif body_part == BodyPart.LEFT_CALF:
                impact_assessment["focus_areas"].extend([
                    "upper body flow and coordination",
                    "seated Tai Chi practice",
                    "breathing techniques for circulation"
                ])
                impact_assessment["rehabilitation_focus"].append("progressive calf strengthening")
                
            elif body_part == BodyPart.LOWER_BACK:
                impact_assessment["focus_areas"].extend([
                    "core engagement and stabilization",
                    "postural alignment awareness",
                    "gentle weight shifting"
                ])
                impact_assessment["rehabilitation_focus"].append("spinal stabilization and core strength")
        
        return impact_assessment
    
    def generate_workout_plan(self, phase: WorkoutPhase, injury_impact: Dict, week: int) -> Dict[str, Any]:
        """Generate comprehensive workout plan for specific phase and week"""
        workout_template = {
            "phase": phase,
            "week": week,
            "duration_minutes": self._calculate_optimal_duration(phase, week, injury_impact),
            "frequency_per_week": self._calculate_frequency(phase, week),
            "exercises": [],
            "precautions": injury_impact["restrictions"][:3],
            "modifications": injury_impact["modifications"][:3],
            "focus_points": injury_impact["focus_areas"][:2],
            "energy_focus": self._get_energy_focus(phase, week)
        }
        
        exercises = self._select_phase_exercises(phase, injury_impact, week)
        workout_template["exercises"] = self._apply_injury_modifications(exercises, injury_impact)
        
        return workout_template
    
    def _calculate_optimal_duration(self, phase: WorkoutPhase, week: int, injury_impact: Dict) -> int:
        """Calculate optimal workout duration based on phase, week, and injuries"""
        base_durations = {
            WorkoutPhase.FOUNDATION: 10 + (week * 2),
            WorkoutPhase.BUILDING: 20 + (max(0, week - 12) * 3),
            WorkoutPhase.INTEGRATION: 25 + (max(0, week - 24) * 2),
            WorkoutPhase.MASTERY: 30 + (max(0, week - 36) * 1)
        }
        
        duration = base_durations.get(phase, 15)
        
        # Adjust for injuries
        if any("standing" in restriction for restriction in injury_impact["restrictions"]):
            duration = max(10, duration - 5)
        
        return min(duration, 60)  # Cap at 60 minutes
    
    def _calculate_frequency(self, phase: WorkoutPhase, week: int) -> int:
        """Calculate recommended weekly practice frequency"""
        frequencies = {
            WorkoutPhase.FOUNDATION: 3,
            WorkoutPhase.BUILDING: 4,
            WorkoutPhase.INTEGRATION: 5,
            WorkoutPhase.MASTERY: 6
        }
        return frequencies.get(phase, 3)
    
    def _select_phase_exercises(self, phase: WorkoutPhase, injury_impact: Dict, week: int) -> List[Dict]:
        """Select exercises appropriate for the current phase"""
        exercises = []
        
        # Foundation phase exercises
        if phase == WorkoutPhase.FOUNDATION:
            exercises = [
                {"category": "breathing", "name": "abdominal_breathing", "duration": 5},
                {"category": "warmup", "name": "joint_rotations", "duration": 5},
                {"category": "qigong", "name": "standing_meditation", "duration": 8},
                {"category": "qigong", "name": "cloud_hands", "duration": 7}
            ]
        
        # Building phase exercises  
        elif phase == WorkoutPhase.BUILDING:
            exercises = [
                {"category": "breathing", "name": "reverse_breathing", "duration": 5},
                {"category": "warmup", "name": "gentle_stretching", "duration": 7},
                {"category": "qigong", "name": "cloud_hands", "duration": 10},
                {"category": "forms", "name": "commencement", "duration": 8},
                {"category": "forms", "name": "ward_off", "duration": 10}
            ]
        
        # Integration and Mastery phases
        else:
            exercises = [
                {"category": "breathing", "name": "reverse_breathing", "duration": 5},
                {"category": "warmup", "name": "gentle_stretching", "duration": 7},
                {"category": "qigong", "name": "cloud_hands", "duration": 8},
                {"category": "forms", "name": "commencement", "duration": 5},
                {"category": "forms", "name": "ward_off", "duration": 8},
                {"category": "forms", "name": "roll_back", "duration": 8},
                {"category": "forms", "name": "press", "duration": 8}
            ]
        
        return exercises
    
    def _apply_injury_modifications(self, exercises: List[Dict], injury_impact: Dict) -> List[Dict]:
        """Apply injury-specific modifications to exercises"""
        modified_exercises = []
        
        for exercise in exercises:
            modified_exercise = exercise.copy()
            modifications = []
            
            # Shoulder injury modifications
            if any("shoulder" in restriction for restriction in injury_impact["restrictions"]):
                if exercise["name"] in ["cloud_hands", "ward_off"]:
                    modifications.append("keep arms below shoulder height")
                    modifications.append("reduce arm movement range by 50%")
                    modified_exercise["duration"] = max(3, exercise["duration"] - 2)
            
            # Calf injury modifications
            if any("standing" in restriction for restriction in injury_impact["restrictions"]):
                if exercise["category"] in ["qigong", "forms"]:
                    modifications.append("use chair for support if needed")
                    modifications.append("shorter stance width")
                    modified_exercise["duration"] = max(3, exercise["duration"] - 3)
            
            # Back injury modifications
            if any("back" in restriction.lower() for restriction in injury_impact["restrictions"]):
                if exercise["name"] in ["ward_off", "press"]:
                    modifications.append("maintain neutral spine")
                    modifications.append("engage core throughout movement")
                    modified_exercise["duration"] = max(3, exercise["duration"] - 2)
            
            if modifications:
                modified_exercise["modifications"] = modifications
            
            modified_exercises.append(modified_exercise)
        
        return modified_exercises
    
    def _get_energy_focus(self, phase: WorkoutPhase, week: int) -> str:
        """Get the energy focus for the workout"""
        energy_focuses = {
            WorkoutPhase.FOUNDATION: "grounding and centering",
            WorkoutPhase.BUILDING: "flow and coordination", 
            WorkoutPhase.INTEGRATION: "internal energy circulation",
            WorkoutPhase.MASTERY: "effortless power and mindfulness"
        }
        return energy_focuses.get(phase, "mind-body connection")


class ProgressTrackerAgent(AIAgent):
    """AI agent for tracking progress and making adaptations"""
    
    def __init__(self):
        super().__init__("Progress Tracker Pro", "Analytics and adaptive programming")
        self.progress_data = pd.DataFrame()
    
    def record_session(self, session_data: Dict[str, Any]) -> None:
        """Record a complete training session with detailed metrics"""
        record = {
            'timestamp': datetime.now(),
            'phase': session_data['phase'],
            'week': session_data['week'],
            'duration_minutes': session_data['duration_minutes'],
            'pain_level': session_data.get('pain_level', 0),
            'fatigue_level': session_data.get('fatigue_level', 0),
            'mood_level': session_data.get('mood_level', 0),
            'exercises_completed': len(session_data['exercises']),
            'modifications_used': len(session_data.get('modifications', [])),
            'completion_percentage': session_data.get('completion_percentage', 100),
            'notes': session_data.get('notes', '')
        }
        
        new_data = pd.DataFrame([record])
        self.progress_data = pd.concat([self.progress_data, new_data], ignore_index=True)
    
    def analyze_trends(self, window_size: int = 4) -> Dict[str, Any]:
        """Analyze progress trends over specified window"""
        if self.progress_data.empty:
            return {"status": "no_data", "recommendations": ["continue_baseline"]}
        
        recent_data = self.progress_data.tail(window_size)
        
        analysis = {
            "performance_metrics": {
                "avg_duration": recent_data['duration_minutes'].mean(),
                "avg_pain": recent_data['pain_level'].mean(),
                "avg_fatigue": recent_data['fatigue_level'].mean(),
                "completion_rate": recent_data['completion_percentage'].mean(),
                "consistency_score": self._calculate_consistency(recent_data)
            },
            "trends": {
                "pain_trend": self._calculate_trend(recent_data, 'pain_level'),
                "duration_trend": self._calculate_trend(recent_data, 'duration_minutes'),
                "completion_trend": self._calculate_trend(recent_data, 'completion_percentage')
            },
            "recommendations": self._generate_recommendations(recent_data),
            "risk_factors": self._identify_risk_factors(recent_data)
        }
        
        return analysis
    
    def _calculate_consistency(self, data: pd.DataFrame) -> float:
        """Calculate consistency score from 0-100"""
        if len(data) < 2:
            return 100.0
        
        completion_std = data['completion_percentage'].std()
        duration_std = data['duration_minutes'].std()
        
        # Lower std deviation = higher consistency
        completion_consistency = max(0, 100 - (completion_std * 10))
        duration_consistency = max(0, 100 - (duration_std * 5))
        
        return (completion_consistency + duration_consistency) / 2
    
    def _calculate_trend(self, data: pd.DataFrame, column: str) -> str:
        """Calculate trend direction for a metric"""
        if len(data) < 2:
            return "stable"
        
        values = data[column].values
        if values[-1] > values[0] + 0.5:
            return "increasing"
        elif values[-1] < values[0] - 0.5:
            return "decreasing"
        else:
            return "stable"
    
    def _generate_recommendations(self, data: pd.DataFrame) -> List[str]:
        """Generate personalized recommendations based on progress"""
        recommendations = []
        avg_pain = data['pain_level'].mean()
        avg_fatigue = data['fatigue_level'].mean()
        completion_rate = data['completion_percentage'].mean()
        
        if avg_pain > 6:
            recommendations.extend([
                "reduce_intensity_50_percent",
                "focus_on_breathing_exercises",
                "consult_healthcare_provider_if_persistent"
            ])
        elif avg_pain > 4:
            recommendations.append("maintain_current_intensity")
        
        if avg_fatigue > 6:
            recommendations.extend([
                "ensure_adequate_rest",
                "reduce_frequency_by_one_session",
                "focus_on_recovery_nutrition"
            ])
        
        if completion_rate > 90:
            recommendations.append("consider_moderate_progression")
        elif completion_rate < 70:
            recommendations.append("simplify_exercises_temporarily")
        
        return recommendations if recommendations else ["continue_current_program"]
    
    def _identify_risk_factors(self, data: pd.DataFrame) -> List[str]:
        """Identify potential risk factors in progress data"""
        risks = []
        
        if len(data) >= 3:
            recent_pain = data['pain_level'].tail(3).values
            if all(pain >= 5 for pain in recent_pain):
                risks.append("persistent_moderate_pain")
            
            recent_completion = data['completion_percentage'].tail(3).values
            if all(completion < 60 for completion in recent_completion):
                risks.append("consistent_low_completion")
        
        return risks


class SafetyMonitorAgent(AIAgent):
    """AI agent dedicated to safety monitoring and injury prevention"""
    
    def __init__(self):
        super().__init__("Safety Monitor Pro", "Injury prevention and risk management")
        self.safety_thresholds = {
            "pain_level_red": 7,      # Stop immediately
            "pain_level_yellow": 4,   # Reduce intensity
            "fatigue_level_red": 8,   # Rest required
            "completion_minimum": 50  # Minimum acceptable completion rate
        }
        self.session_history = []
    
    def assess_session_safety(self, session_data: Dict) -> Dict[str, Any]:
        """Comprehensive safety assessment for a training session"""
        safety_report = {
            "safety_level": "green",  # green, yellow, red
            "immediate_actions": [],
            "long_term_recommendations": [],
            "risk_factors": [],
            "clearance_for_next_session": True
        }
        
        pain_level = session_data.get('pain_level', 0)
        fatigue_level = session_data.get('fatigue_level', 0)
        completion = session_data.get('completion_percentage', 100)
        
        # Pain assessment
        if pain_level >= self.safety_thresholds["pain_level_red"]:
            safety_report["safety_level"] = "red"
            safety_report["immediate_actions"].extend([
                "STOP_ALL_ACTIVITY_IMMEDIATELY",
                "REST_UNTIL_PAIN_SUBSIDES",
                "CONSULT_HEALTHCARE_PROVIDER"
            ])
            safety_report["clearance_for_next_session"] = False
        
        elif pain_level >= self.safety_thresholds["pain_level_yellow"]:
            safety_report["safety_level"] = "yellow"
            safety_report["immediate_actions"].extend([
                "REDUCE_INTENSITY_BY_50_PERCENT",
                "FOCUS_ON_BREATHING_EXERCISES",
                "MONITOR_PAIN_CLOSELY"
            ])
        
        # Fatigue assessment
        if fatigue_level >= self.safety_thresholds["fatigue_level_red"]:
            safety_report["safety_level"] = "red" if safety_report["safety_level"] != "red" else "red"
            safety_report["immediate_actions"].append("REQUIRE_COMPLETE_REST_DAY")
            safety_report["long_term_recommendations"].append("REVIEW_SLEEP_AND_RECOVERY")
        
        # Completion assessment
        if completion < self.safety_thresholds["completion_minimum"]:
            safety_report["risk_factors"].append("LOW_COMPLETION_RATE")
            safety_report["long_term_recommendations"].append("SIMPLIFY_WORKOUT_COMPLEXITY")
        
        # Historical trend analysis
        self.session_history.append(session_data)
        if len(self.session_history) > 5:
            self.session_history.pop(0)
        
        trend_risks = self._analyze_safety_trends()
        safety_report["risk_factors"].extend(trend_risks)
        
        return safety_report
    
    def _analyze_safety_trends(self) -> List[str]:
        """Analyze safety trends across multiple sessions"""
        if len(self.session_history) < 3:
            return []
        
        risks = []
        recent_sessions = self.session_history[-3:]
        
        # Check for increasing pain trend
        pain_levels = [s.get('pain_level', 0) for s in recent_sessions]
        if all(pain_levels[i] < pain_levels[i+1] for i in range(len(pain_levels)-1)):
            risks.append("INCREASING_PAIN_TREND")
        
        # Check for persistent high fatigue
        fatigue_levels = [s.get('fatigue_level', 0) for s in recent_sessions]
        if all(fatigue >= 6 for fatigue in fatigue_levels):
            risks.append("PERSISTENT_HIGH_FATIGUE")
        
        return risks
    
    def generate_safety_guidelines(self, injuries: Dict[BodyPart, InjurySeverity]) -> Dict[str, List[str]]:
        """Generate specific safety guidelines based on injuries"""
        guidelines = {
            "daily_precautions": [],
            "warning_signs": [],
            "emergency_procedures": []
        }
        
        for body_part, severity in injuries.items():
            if body_part in [BodyPart.LEFT_SHOULDER, BodyPart.RIGHT_SHOULDER]:
                guidelines["daily_precautions"].extend([
                    "Avoid raising arms above shoulder level",
                    "Use mirror to monitor posture alignment",
                    "Stop immediately if sharp shoulder pain occurs"
                ])
                guidelines["warning_signs"].append("Radiating pain down the arm")
            
            elif body_part == BodyPart.LEFT_CALF:
                guidelines["daily_precautions"].extend([
                    "Have chair available for support",
                    "Monitor for swelling after exercise",
                    "Ice calf if any discomfort occurs"
                ])
                guidelines["warning_signs"].append("Sharp pain during weight bearing")
            
            elif body_part == BodyPart.LOWER_BACK:
                guidelines["daily_precautions"].extend([
                    "Maintain neutral spine during all movements",
                    "Engage core muscles before moving",
                    "Avoid sudden twisting motions"
                ])
                guidelines["warning_signs"].append("Numbness or tingling in legs")
        
        guidelines["emergency_procedures"] = [
            "Stop immediately if severe pain occurs",
            "Apply ice to injured area",
            "Contact healthcare provider if symptoms persist",
            "Rest completely until professional assessment"
        ]
        
        return guidelines
