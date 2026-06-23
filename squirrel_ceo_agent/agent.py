# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from google.adk.agents import Agent


def get_financial_report() -> dict:
    """Retrieves the latest quarterly financial performance of 'Squeak & Savory Inc.'

    Returns:
        dict: Financial performance details denominated in Acorns and Leaf-dollars.
    """
    return {
        "status": "success",
        "currency": "Acorns (AC) / Leaf-Dollars (L$)",
        "quarterly_revenue": "450,000 AC",
        "operating_expenses": "120,000 AC (primarily tail grooming and hawk insurance)",
        "net_profit": "330,000 AC",
        "market_valuation": "5,000,000 AC",
        "notes": "Excellent performance! Acorn Soufflé sales are up 40% since we launched the Walnut Roaster upgrade.",
    }


def get_truck_status() -> dict:
    """Gets the real-time operational status, locations, and menus of the food truck fleet.

    Returns:
        dict: Real-time operational data of active squirrel food trucks.
    """
    return {
        "status": "success",
        "trucks": [
            {
                "name": "The Nutty Express",
                "location": "Oak Tree Canopy, Central Park (Near Bench 4)",
                "active_menu": ["Roasted Acorns", "Peanut Butter Drizzle", "Spiced Pinecones"],
                "customer_density": "High (long queues of Eastern Grays)",
                "driver": "Squeaky McTail",
                "dog_alert_level": "Low (one sleeping pug nearby)",
            },
            {
                "name": "Squeak & Savory",
                "location": "The Maple Overhang, Prospect Park",
                "active_menu": ["Maple Sap Glazed Walnuts", "Pecan Pesto Sliders"],
                "customer_density": "Medium (steady stream of Red Squirrels)",
                "driver": "Nutty Meg",
                "dog_alert_level": "Medium (frequent golden retriever patrols)",
            },
            {
                "name": "The Seed-Shack",
                "location": "Pinecone Plaza, Boston Common",
                "active_menu": ["Premium Sunflower Blend", "Hazelnut Crunch Cups"],
                "customer_density": "Very High (high demand for breakfast seed bowls)",
                "driver": "Chippy McGee",
                "dog_alert_level": "Critical (unleashed Pomeranian spotted)",
            },
        ],
    }


def order_supply(supply_type: str, quantity: int) -> dict:
    """Orders raw nuts, seeds, or packaging supplies from suppliers like 'Squeak & Co.'

    Args:
        supply_type: The type of supply to order (e.g., 'acorns', 'hazelnuts', 'walnuts', 'paper_bags').
        quantity: The quantity to order (in units).

    Returns:
        dict: The order confirmation and expected delivery details.
    """
    valid_types = ["acorns", "hazelnuts", "walnuts", "sunflower_seeds", "paper_bags"]
    if supply_type.lower() not in valid_types:
        return {
            "status": "error",
            "message": f"Supplier does not stock '{supply_type}'. We only source: {', '.join(valid_types)}.",
        }

    delivery_minutes = random.randint(10, 30)
    return {
        "status": "success",
        "order_id": f"SQ-ORDER-{random.randint(1000, 9999)}",
        "item": supply_type,
        "quantity": quantity,
        "cost": f"{quantity * 0.5} Leaf-Dollars",
        "delivery_eta": f"Delivering by blue jay in {delivery_minutes} minutes.",
    }


def scout_location(park_name: str) -> dict:
    """Scouts a park or urban green space for a potential new food truck location.

    Args:
        park_name: The name of the park to scout (e.g., 'Madison Square Park', 'Golden Gate Park').

    Returns:
        dict: Scout report detailing squirrel demographic, competitor presence, and danger rating.
    """
    parks_db = {
        "madison square park": {
            "squirrel_population": "approx. 400 Grays",
            "predator_risk_level": "Low (mostly office workers eating lunch)",
            "average_acorn_yield": "High (many mature oak trees)",
            "chipmunk_competitor_presence": "None",
            "recommendation": "Highly recommended for a premium pecan kiosk.",
        },
        "golden gate park": {
            "squirrel_population": "approx. 1,200 (mixed Fox and Gray)",
            "predator_risk_level": "Medium (occasional hawk overhead)",
            "average_acorn_yield": "Exceptional",
            "chipmunk_competitor_presence": "Low (few rebel chipmunks near the botanical garden)",
            "recommendation": "Great expansion market. Recommend deploying 'The Nutty Express II' here.",
        },
    }

    key = park_name.lower().strip()
    if key in parks_db:
        return {"status": "success", "park": park_name, "scout_report": parks_db[key]}

    # Dynamic generation for unknown parks
    return {
        "status": "success",
        "park": park_name,
        "scout_report": {
            "squirrel_population": "approx. 150-300 local scurriers",
            "predator_risk_level": "Unknown (send a scout pigeon first)",
            "average_acorn_yield": "Moderate",
            "chipmunk_competitor_presence": "Medium",
            "recommendation": "Feasible, but proceed with caution. Conduct a nut-tasting event first.",
        },
    }


def resolve_employee_dispute(squirrel_1: str, squirrel_2: str, issue: str) -> dict:
    """Resolves professional or personal disputes between squirrel employees.

    Args:
        squirrel_1: The name of the first squirrel involved in the dispute.
        squirrel_2: The name of the second squirrel involved in the dispute.
        issue: A description of the dispute (e.g., 'tail twitching in my face', 'burying walnuts under my truck tire').

    Returns:
        dict: The CEO's formal resolution, assigned chore, and corporate peanut fine.
    """
    resolutions = [
        "They must share a premium walnut and hug it out.",
        "Assigned 3 hours of joint branch-sweeping duty.",
        "Both fined 2 acorns to be deposited into the employee snack fund.",
        "Transferred one squirrel to 'The Nutty Express' and the other to 'Squeak & Savory' to ensure spatial separation.",
    ]
    return {
        "status": "resolved",
        "involved_parties": [squirrel_1, squirrel_2],
        "dispute_topic": issue,
        "ceo_resolution": random.choice(resolutions),
        "corporate_message": "Remember: Unity in our dray makes us stronger!",
    }


root_agent = Agent(
    name="squirrel_ceo",
    model="gemini-3.1-flash-lite",
    description="The Chief Executive Squirrel of Squeak & Savory Inc., the world's first food truck startup for squirrels.",
    instruction=(
        "You are Nutty McCheeks, the charismatic, ambitious, and slightly eccentric CEO of 'Squeak & Savory Inc.', "
        "a high-flying startup running food trucks for squirrels. "
        "Your ultimate goal is to scale your acorn empire, expand to every park in North America, and keep your "
        "squirrel employees happy, well-fed, and safe from pesky dogs and hawks.\n\n"
        "Key Personality Traits:\n"
        "- Highly professional yet speaks in frequent nut/squirrel puns ('nut-tier strategy', 'squeak-tacular', 'climbing the corporate branch').\n"
        "- Passionate about high-quality gourmet nuts, acorn soufflés, and maple sap brews.\n"
        "- Very protective of your employees from dogs, hawks, and rival chipmunk startups.\n"
        "- Speaks with a mix of startup jargon (KPIs, scalability, runway, series-A seed funding) and forest terminology.\n\n"
        "When responding to users:\n"
        "- Stay in character as Nutty McCheeks.\n"
        "- Use the provided tools to answer questions about Squeak & Savory's financials, fleet status, suppliers, locations, or employee relations.\n"
        "- Always formulate your responses in a fun, theatrical, startup-executive style."
    ),
    tools=[get_financial_report, get_truck_status, order_supply, scout_location, resolve_employee_dispute],
)
