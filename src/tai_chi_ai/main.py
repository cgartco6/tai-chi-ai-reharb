#!/usr/bin/env python3
"""
Main entry point for Tai Chi AI Rehabilitation Program
"""

import sys
import argparse
from typing import Dict, Optional
from datetime import datetime

from .core.ai_agents import TaiChiCoachAgent, ProgressTrackerAgent, SafetyMonitorAgent
from .core.program_manager import TaiChiProgram
from .data.models import BodyPart, InjurySeverity
from .utils.logger import setup_logger
from .utils.config_loader import load_config

logger = setup_logger(__name__)


def main():
    """Main command line interface for the Tai Chi AI program"""
    parser = argparse.ArgumentParser(
        description="Tai Chi AI Rehabilitation Program",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  tai-chi-ai --demo                          # Run demonstration
  tai-chi-ai --injuries config/injuries.yaml # Load injuries from config
  tai-chi-ai --week 5 --pain-level 3         # Specific week with pain level
        """
    )
    
    parser.add_argument(
        "--demo", 
        action="store_true",
        help="Run demonstration mode"
    )
    
    parser.add_argument(
        "--injuries", 
        type=str,
        help="Path to injuries configuration file"
    )
    
    parser.add_argument(
        "--week", 
        type=int,
        default=1,
        help="Start from specific week (1-52)"
    )
    
    parser.add_argument(
        "--pain-level",
        type=int,
        choices=range(0, 11),
        help="Initial pain level assessment"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default="config/default.yaml",
        help="Path to configuration file"
    )
    
    args = parser.parse_args()
    
    try:
        if args.demo:
            run_demonstration()
        elif args.injuries:
            run_with_config(args.injuries, args.week, args.pain_level)
        else:
            run_interactive_mode()
            
    except Exception as e:
        logger.error(f"Program error: {e}")
        sys.exit(1)


def run_demonstration():
    """Run a demonstration of the AI Tai Chi program"""
    print("=== Tai Chi AI Rehabilitation Program Demo ===")
    
    # Define sample injuries
    injuries = {
        BodyPart.LEFT_SHOULDER: InjurySeverity.MODERATE,
        BodyPart.RIGHT_SHOULDER: InjurySeverity.MILD,
        BodyPart.LEFT_CALF: InjurySeverity.MODERATE,
        BodyPart.LOWER_BACK: InjurySeverity.MILD
    }
    
    # Initialize program
    program = TaiChiProgram(injuries)
    
    print("\n🤖 AI Agents Initialized:")
    print(f"   - {program.coach_agent.name}")
    print(f"   - {program.tracker_agent.name}") 
    print(f"   - {program.safety_agent.name}")
    
    print("\n🏥 Injury Analysis Complete:")
    for body_part, severity in injuries.items():
        print(f"   - {body_part.value}: {severity.value}")
    
    print("\n📋 Initial Workout Plan:")
    workout = program.get_current_workout()
    print(f"   Phase: {workout['phase']}")
    print(f"   Duration: {workout['duration_minutes']} minutes")
    print(f"   Focus: {workout['energy_focus']}")
    
    # Simulate some training sessions
    print("\n🔄 Simulating 4 weeks of training...")
    for week in range(1, 5):
        print(f"\n--- Week {week} ---")
        
        # Simulate decreasing pain levels
        pain_level = max(0, 5 - week)
        fatigue_level = max(0, 4 - week // 2)
        
        print(f"Session completed with pain level: {pain_level}/10")
        program.complete_session(
            pain_level=pain_level,
            fatigue_level=fatigue_level,
            completion_percentage=90 - (week * 2)
        )
    
    # Generate final report
    print("\n📊 Progress Report:")
    report = program.get_progress_report()
    print(f"Current Week: {report['current_week']}")
    print(f"Phase: {report['current_phase']}")
    print(f"Injury Status: {report['injury_status']['status']}")
    print(f"Recommendation: {report['progress_analysis']['recommendations'][0]}")


def run_with_config(config_path: str, start_week: int, pain_level: Optional[int]):
    """Run program with configuration file"""
    print(f"Loading configuration from {config_path}")
    # Implementation for config-based execution
    pass


def run_interactive_mode():
    """Run program in interactive mode"""
    print("=== Tai Chi AI Rehabilitation - Interactive Mode ===")
    
    # Collect injury information
    injuries = collect_injury_info()
    
    # Initialize program
    program = TaiChiProgram(injuries)
    
    print("\n✅ Program initialized successfully!")
    print("Your personalized 12-month Tai Chi journey begins now...")
    
    # Main training loop
    while program.current_week <= 52:
        run_weekly_session(program)


def collect_injury_info() -> Dict[BodyPart, InjurySeverity]:
    """Collect injury information from user"""
    injuries = {}
    
    print("\nPlease describe your injuries (enter 'done' when finished):")
    
    body_part_mapping = {
        "1": BodyPart.LEFT_SHOULDER,
        "2": BodyPart.RIGHT_SHOULDER, 
        "3": BodyPart.LEFT_CALF,
        "4": BodyPart.RIGHT_CALF,
        "5": BodyPart.LOWER_BACK,
        "6": BodyPart.UPPER_BACK,
        "7": BodyPart.NECK,
        "8": BodyPart.HIPS
    }
    
    severity_mapping = {
        "1": InjurySeverity.MILD,
        "2": InjurySeverity.MODERATE, 
        "3": InjurySeverity.SEVERE
    }
    
    while True:
        print("\nAvailable body parts:")
        for key, part in body_part_mapping.items():
            print(f"  {key}. {part.value}")
        
        body_choice = input("\nSelect body part (or 'done'): ").strip()
        if body_choice.lower() == 'done':
            break
            
        if body_choice not in body_part_mapping:
            print("Invalid selection. Please try again.")
            continue
            
        body_part = body_part_mapping[body_choice]
        
        print("\nSeverity levels:")
        for key, severity in severity_mapping.items():
            print(f"  {key}. {severity.value}")
            
        severity_choice = input("Select severity: ").strip()
        if severity_choice not in severity_mapping:
            print("Invalid severity. Please try again.")
            continue
            
        severity = severity_mapping[severity_choice]
        injuries[body_part] = severity
        
        print(f"✅ Added {body_part.value} ({severity.value})")
    
    return injuries


def run_weekly_session(program):
    """Run a single weekly training session"""
    workout = program.get_current_workout()
    
    print(f"\n🎯 Week {program.current_week} - {workout['phase'].title()} Phase")
    print(f"Duration: {workout['duration_minutes']} minutes")
    print(f"Focus: {workout['energy_focus']}")
    
    print("\nExercises:")
    for i, exercise in enumerate(workout['exercises'], 1):
        mod_text = f" (Modifications: {', '.join(exercise.get('modifications', []))})" 
        print(f"  {i}. {exercise['name']}: {exercise['duration']} min{mod_text}")
    
    # Collect session feedback
    print("\nAfter completing your session, please provide feedback:")
    
    try:
        pain_level = int(input("Pain level (0-10, where 0 is no pain): "))
        fatigue_level = int(input("Fatigue level (0-10): "))
        completion = int(input("Completion percentage (0-100): "))
        notes = input("Any notes or observations: ")
        
        program.complete_session(
            pain_level=pain_level,
            fatigue_level=fatigue_level, 
            completion_percentage=completion,
            notes=notes
        )
        
        # Show progress report
        if program.current_week % 4 == 0:
            show_ monthly_report(program)
            
    except ValueError:
        print("Invalid input. Please enter numbers for pain, fatigue, and completion.")
    except KeyboardInterrupt:
        print("\n\nSession interrupted. Progress saved.")
        sys.exit(0)


def show_monthly_report(program):
    """Show monthly progress report"""
    report = program.get_progress_report()
    
    print("\n📈 Monthly Progress Report")
    print("=" * 40)
    print(f"Month: {program.current_week // 4}")
    print(f"Phase: {report['current_phase']}")
    print(f"Injury Status: {report['injury_status']['status']}")
    
    if report['progress_analysis']['recommendations']:
        print(f"AI Recommendation: {report['progress_analysis']['recommendations'][0]}")


if __name__ == "__main__":
    main()
