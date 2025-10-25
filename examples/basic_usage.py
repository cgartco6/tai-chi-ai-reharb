#!/usr/bin/env python3
"""
Basic usage example for Tai Chi AI Rehabilitation Program
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tai_chi_ai import TaiChiProgram
from tai_chi_ai.data.models import BodyPart, InjurySeverity


def main():
    """Demonstrate basic usage of the Tai Chi AI program"""
    
    print("=== Tai Chi AI Rehabilitation - Basic Usage Example ===")
    
    # Step 1: Define injuries
    injuries = {
        BodyPart.LEFT_SHOULDER: InjurySeverity.MODERATE,
        BodyPart.RIGHT_SHOULDER: InjurySeverity.MILD, 
        BodyPart.LEFT_CALF: InjurySeverity.MODERATE,
        BodyPart.LOWER_BACK: InjurySeverity.MILD
    }
    
    print("\n1. Initializing program with injuries:")
    for body_part, severity in injuries.items():
        print(f"   - {body_part.value}: {severity.value}")
    
    # Step 2: Create program
    program = TaiChiProgram(injuries)
    
    # Step 3: Get first workout
    print("\n2. Generated Workout Plan:")
    workout = program.get_current_workout()
    
    print(f"   Phase: {workout['phase']}")
    print(f"   Week: {workout['week']}")
    print(f"   Duration: {workout['duration_minutes']} minutes")
    print(f"   Energy Focus: {workout['energy_focus']}")
    
    print("\n   Exercises:")
    for i, exercise in enumerate(workout['exercises'], 1):
        mods = exercise.get('modifications', [])
        mod_text = f" (modifications: {', '.join(mods)})" if mods else ""
        print(f"   {i}. {exercise['name']}: {exercise['duration']} min{mod_text}")
    
    # Step 4: Simulate completing sessions
    print("\n3. Simulating training sessions...")
    
    session_data = [
        {"pain": 4, "fatigue": 3, "completion": 85},
        {"pain": 3, "fatigue": 2, "completion": 90},
        {"pain": 2, "fatigue": 2, "completion": 95},
        {"pain": 1, "fatigue": 1, "completion": 100}
    ]
    
    for i, data in enumerate(session_data, 1):
        print(f"\n   Session {i}:")
        print(f"     Pain: {data['pain']}/10")
        print(f"     Fatigue: {data['fatigue']}/10") 
        print(f"     Completion: {data['completion']}%")
        
        program.complete_session(
            pain_level=data['pain'],
            fatigue_level=data['fatigue'],
            completion_percentage=data['completion']
        )
    
    # Step 5: Get progress report
    print("\n4. Progress Report:")
    report = program.get_progress_report()
    
    print(f"   Current Week: {report['current_week']}")
    print(f"   Current Phase: {report['current_phase']}")
    print(f"   Injury Status: {report['injury_status']['status']}")
    
    if report['progress_analysis']['recommendations']:
        rec = report['progress_analysis']['recommendations'][0]
        print(f"   AI Recommendation: {rec}")
    
    print("\n✅ Example completed successfully!")
    print("Your personalized Tai Chi journey is ready to begin.")


if __name__ == "__main__":
    main()
