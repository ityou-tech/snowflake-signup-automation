#!/usr/bin/env python3
"""
Generate random test data for the Snowflake signup process.
"""

import argparse
import json
import random
import string
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# Sample data for random generation
FIRST_NAMES = [
    "Alex", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Dakota", "Quinn",
    "Avery", "Charlie", "Sam", "Jamie", "Pat", "Drew", "Cameron", "Jesse",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson",
    "Taylor", "Clark", "Walker", "Hall", "Young", "Allen", "King", "Wright",
    "Lee", "Scott", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell", "Perez",
    "Garcia", "Rodriguez", "Lopez", "Martinez", "Hernandez", "Moore", "Martin",
]

DOMAINS = [
    "example.com", "test.org", "sample.net", "demo.io", "verify.co", "trial.dev",
]

COMPANIES = [
    "TechCorp", "DataSystems", "InfoTech", "CloudWorks", "ByteLogic", "CodeNest",
    "SynthLogic", "NetMatrix", "DataFlow", "InfoSystems", "TechNexus", "ByteWave",
    "Quantum Data", "Matrix Systems", "Logic Stream", "InfoFusion", "SynthData",
]

JOB_TITLES = [
    "Data Engineer", "System Administrator", "Cloud Architect", "DevOps Engineer",
    "Database Administrator", "Data Scientist", "Software Engineer", "IT Manager",
    "Business Analyst", "Data Analyst", "Solutions Architect", "IT Specialist",
]

def random_email(first_name: str, last_name: str) -> str:
    """Generate a random email address."""
    options = [
        f"{first_name.lower()}{random.randint(1, 999)}@{random.choice(DOMAINS)}",
        f"{first_name.lower()}.{last_name.lower()}@{random.choice(DOMAINS)}",
        f"{first_name[0].lower()}{last_name.lower()}@{random.choice(DOMAINS)}",
    ]
    return random.choice(options)

def generate_test_data(count: int = 1) -> List[Dict[str, str]]:
    """Generate test data entries."""
    entries = []
    
    for _ in range(count):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        
        entry = {
            "first_name": first_name,
            "last_name": last_name,
            "email": random_email(first_name, last_name),
            "company": random.choice(COMPANIES),
            "job_title": random.choice(JOB_TITLES),
        }
        
        entries.append(entry)
    
    return entries

def main() -> None:
    """Main function for the test data generator."""
    parser = argparse.ArgumentParser(description="Generate test data for Snowflake signup")
    parser.add_argument("-c", "--count", type=int, default=3, help="Number of test data entries to generate")
    parser.add_argument("-o", "--output", default="test_data.json", help="Output JSON file path")
    parser.add_argument("-p", "--print", action="store_true", help="Print the generated data to console")
    args = parser.parse_args()
    
    # Generate the test data
    data = generate_test_data(args.count)
    output_data = {
        "generated_at": datetime.now().isoformat(),
        "test_data": data,
    }
    
    # Print to console if requested
    if args.print:
        print(json.dumps(output_data, indent=2))
    
    # Save to file
    output_path = Path(args.output)
    with open(output_path, "w") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"Generated {args.count} test data entries and saved to {output_path}")

if __name__ == "__main__":
    main()