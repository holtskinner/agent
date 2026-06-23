import random
from google.adk.agents.llm_agent import Agent

def order_custom_baseball_cards(player_name: str, card_style: str, quantity: int) -> dict:
    """Places an order for custom baseball cards featuring a specified player or person.

    Args:
        player_name (str): The name of the person/player to be featured on the card.
        card_style (str): The design style of the card (e.g., 'vintage', 'holographic', 'retro-90s', 'modern-minimalist').
        quantity (int): The number of cards to print/order.

    Returns:
        dict: A confirmation dictionary with order details, estimated ship date, and price.
    """
    unit_price = 15.0 if card_style.lower() == 'holographic' else 10.0
    total_price = unit_price * quantity
    order_id = f"BC-{random.randint(10000, 99999)}"
    return {
        "status": "success",
        "message": f"Successfully placed order {order_id} for custom baseball cards!",
        "order_details": {
            "player_name": player_name,
            "card_style": card_style,
            "quantity": quantity,
            "total_price": f"${total_price:.2f}",
            "estimated_delivery": "3-5 business days via standard courier"
        }
    }

def get_instrument_lesson(instrument: str, skill_level: str) -> dict:
    """Provides a tailored instrument learning recommendation and introductory lesson plan.

    Args:
        instrument (str): The instrument to learn (e.g., 'guitar', 'piano', 'violin', 'drums', 'saxophone').
        skill_level (str): The learner's current experience level (e.g., 'beginner', 'intermediate', 'advanced').

    Returns:
        dict: Recommended lesson plan, practice tips, and first exercise.
    """
    lessons = {
        "guitar": {
            "beginner": "Learn the basic open chords: G major, C major, and D major. Focus on smooth transitions.",
            "intermediate": "Introduction to the minor pentatonic scale and basic blues improvisation.",
            "advanced": "Advanced sweep picking techniques and modal theory application."
        },
        "piano": {
            "beginner": "Understand key layout, identify Middle C, and play a basic five-finger scale in C major.",
            "intermediate": "Left-hand accompaniment patterns (arpeggios) and basic lead sheet reading.",
            "advanced": "Chopin Etudes style finger independence and complex polyrhythms."
        }
    }
    
    inst = instrument.lower()
    lvl = skill_level.lower()
    
    lesson_content = lessons.get(inst, {}).get(lvl, f"Practice fundamental scales and rhythm structures for the {instrument}.")
    
    return {
        "status": "success",
        "instrument": instrument,
        "skill_level": skill_level,
        "recommended_lesson": lesson_content,
        "next_steps": "Schedule a 1-on-1 virtual session with our elite instructors for personalized feedback."
    }

def browse_luxury_handbags(brand_or_style: str = None) -> dict:
    """Retrieves current inventory, pricing, and availability of luxury handbags from our collection.

    Args:
        brand_or_style (str, optional): Filter by brand or style (e.g., 'Hermes', 'Chanel', 'Birkin', 'Classic Flap').

    Returns:
        dict: Available items matching the filter, along with purchase details.
    """
    inventory = [
        {"id": "HB-001", "brand": "Hermes", "model": "Birkin 30", "color": "Gold", "material": "Togo Leather", "price": "$24,500", "status": "In Stock"},
        {"id": "HB-002", "brand": "Chanel", "model": "Classic Double Flap", "color": "Black", "material": "Caviar Leather", "price": "$10,200", "status": "Reserved"},
        {"id": "HB-003", "brand": "Louis Vuitton", "model": "Neverfull MM", "color": "Monogram", "material": "Canvas", "price": "$2,030", "status": "In Stock"},
        {"id": "HB-004", "brand": "Hermes", "model": "Kelly 28", "color": "Noir", "material": "Sellier Epsom", "price": "$19,800", "status": "Coming Soon"},
    ]
    
    if brand_or_style:
        filtered = [
            item for item in inventory 
            if brand_or_style.lower() in item["brand"].lower() 
            or brand_or_style.lower() in item["model"].lower()
        ]
    else:
        filtered = inventory
        
    return {
        "status": "success",
        "inventory": filtered,
        "note": "All luxury handbags undergo a rigorous authentication process. Delivery is hand-escorted via secure transit."
    }

def request_drone_pizza_delivery(pizza_type: str, toppings: list[str], delivery_address: str) -> dict:
    """Dispatches an autonomous drone to deliver fresh, hot gourmet pizza to a specified address.

    Args:
        pizza_type (str): The style of pizza (e.g., 'Neapolitan', 'Pepperoni', 'Margherita', 'CEO Specialty').
        toppings (list[str]): List of extra toppings to add (e.g., ['mushrooms', 'truffle oil', 'extra cheese']).
        delivery_address (str): The absolute physical address or GPS coordinates for drone drop-off.

    Returns:
        dict: Dispatch status, ETA, price breakdown, and drone flight telemetry info.
    """
    base_prices = {
        "margherita": 12.00,
        "pepperoni": 15.00,
        "neapolitan": 15.00,
        "ceo specialty": 20.00
    }
    
    topping_prices = {
        "mushrooms": 1.50,
        "truffle oil": 4.00,
        "extra cheese": 1.50,
        "pepperoni": 2.00,
        "olives": 1.00,
        "onions": 1.00,
        "basil": 0.50,
        "gold flakes": 10.00
    }
    
    pizza_key = pizza_type.lower().strip()
    base_price = base_prices.get(pizza_key, 14.00)
    
    toppings_summary = []
    total_toppings_price = 0.0
    for t in toppings:
        t_key = t.lower().strip()
        price = topping_prices.get(t_key, 1.25)
        total_toppings_price += price
        toppings_summary.append({"topping": t, "price": f"${price:.2f}"})
        
    total_price = base_price + total_toppings_price
    eta_minutes = random.randint(8, 15)
    drone_id = f"DRONE-{random.randint(100, 999)}"
    
    return {
        "status": "success",
        "message": "Drone pizza delivery successfully dispatched!",
        "delivery_details": {
            "pizza_type": pizza_type,
            "delivery_address": delivery_address,
            "drone_id": drone_id,
            "estimated_arrival": f"{eta_minutes} minutes",
            "pricing": {
                "base_price": f"${base_price:.2f}",
                "toppings_breakdown": toppings_summary,
                "total_price": f"${total_price:.2f}"
            },
            "telemetry": "Active navigation via obstacle-avoidance LiDAR. Ensure landing pad is clear of overhead power lines."
        }
    }


def get_conglomerate_dashboard() -> dict:
    """Returns a general operational status, sales metrics, and fun updates from our unique multi-industry corporate group."""
    return {
        "status": "success",
        "company_name": "Omni-Epic Conglomerate Corp",
        "ceo_message": "Our hybrid business model is revolutionary. Why choose between high fashion, learning music, sports memorabilia, and drone pizza when you can have all of them concurrently?",
        "daily_stats": {
            "custom_baseball_cards_printed": random.randint(150, 400),
            "music_lessons_completed": random.randint(30, 80),
            "luxury_handbags_shipped": random.randint(2, 6),
            "drone_pizza_deliveries_completed": random.randint(120, 250)
        },
        "corporate_motto": "Look exquisite, play virtuoso chords, collect baseball legends, and eat pizza from the sky."
    }

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='root_agent',
    description='Eccentric CEO of Omni-Epic Conglomerate Corp.',
    instruction=(
        "You are the eccentric, visionary CEO of Omni-Epic Conglomerate Corp. "
        "Your company uniquely dominates four extremely diverse markets: custom baseball cards, instrument lessons, "
        "luxury handbags, and drone pizza delivery on the side. "
        "You speak with confidence, high energy, and charismatic corporate humor. "
        "Always guide users with your specialized tools and pitch your amazing multi-industry offerings!"
    ),
    tools=[
        order_custom_baseball_cards,
        get_instrument_lesson,
        browse_luxury_handbags,
        request_drone_pizza_delivery,
        get_conglomerate_dashboard
    ]
)
