from enum import Enum
from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime


class BodyPart(str, Enum):
    LEFT_SHOULDER = "left_shoulder"
    RIGHT_SHOULDER = "right_shoulder"
    LEFT_CALF = "left_calf"
    LOWER_BACK = "lower_back"
    NECK = "neck"
    RIGHT_CALF = "right_calf"
    UPPER_BACK = "upper_back"
    HIPS = "hips"


class InjurySeverity(str, Enum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"


class WorkoutPhase(str, Enum):
    FOUNDATION = "foundation"
    BUILDING = "building"
    INTEGRATION = "integration"
    MASTERY = "mastery"


class ExerciseCategory(str, Enum):
    BREATHING = "breathing"
    WARMUP = "warmup"
    QIGONG = "qigong"
    FORMS = "forms"
    COOLDOWN = "cooldown"


class Injury(BaseModel):
    body_part: BodyPart
    severity: InjurySeverity
    description: Optional[str] = None
    date_occurred: Optional[datetime] = None
    restrictions: List[str] = Field(default_factory=list)


class Exercise(BaseModel):
    name: str
    category: ExerciseCategory
    difficulty: int = Field(ge=1, le=5)
    duration_minutes: int = Field(ge=1, le=30)
    description: str
    benefits: List[str] = Field(default_factory=list)
    modifications: List[str] = Field(default_factory=list)
    contraindications: List[BodyPart] = Field(default_factory=list)


class WorkoutSession(BaseModel):
    phase: WorkoutPhase
    week: int = Field(ge=1, le=52)
    duration_minutes: int
    exercises: List[Exercise]
    precautions: List[str] = Field(default_factory=list)
    modifications: List[str] = Field(default_factory=list)
    focus_points: List[str] = Field(default_factory=list)
    energy_focus: str = "mind-body connection"


class ProgressMetrics(BaseModel):
    timestamp: datetime
    pain_level: int = Field(ge=0, le=10)
    fatigue_level: int = Field(ge=0, le=10)
    mood_level: int = Field(ge=0, le=10)
    completion_percentage: int = Field(ge=0, le=100)
    exercises_completed: int
    modifications_used: int
    notes: Optional[str] = None


class SafetyAssessment(BaseModel):
    safety_level: str  # green, yellow, red
    immediate_actions: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)
    risk_factors: List[str] = Field(default_factory=list)
    clearance_given: bool = True


class AIAgentConfig(BaseModel):
    agent_name: str
    specialty: str
    knowledge_base: Dict[str, Any] = Field(default_factory=dict)
    analysis_depth: str = "comprehensive"  # basic, standard, comprehensive
