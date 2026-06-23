from google.adk.agents.llm_agent import Agent

# CEO tools

def get_menu() -> dict:
    """Returns the current catalog of gourmet rat foods with descriptions and pricing."""
    return {
        "status": "success",
        "products": [
            {
                "name": "Truffle-infused Brie Nibbles",
                "price": "$25 per ounce",
                "description": "A luxurious, hand-crafted cheese pairing imported from the finest French sewers."
            },
            {
                "name": "Saffron Oat Risotto",
                "price": "$18 per ounce",
                "description": "Premium rolled oats slow-simmered with Iranian saffron and garnished with edible gold leaf."
            },
            {
                "name": "Caviar-infused Peanut Butter",
                "price": "$30 per jar",
                "description": "Wild-caught sturgeon roe folded into organic, fresh-ground peanut butter."
            },
            {
                "name": "Champagne-fermented Grape Seeds",
                "price": "$15 per bag",
                "description": "Gently crushed chardonnay grape seeds aged to perfection for that bubbly kick."
            },
            {
                "name": "Micro-greens with Gold Leaf Dust",
                "price": "$22 per bowl",
                "description": "A crisp, refreshing salad for the health-conscious rodent of distinction."
            }
        ]
    }

def get_financials() -> dict:
    """Returns the startup's current financial status, growth metrics, and investor projections."""
    return {
        "status": "success",
        "metrics": {
            "company_name": "Gourmet Rodent Co.",
            "current_valuation": "$42 Million",
            "seed_round": "Raised $4.2M from Sequoia-squeak Partners",
            "runway": "18 months",
            "year_over_year_growth": "+340% (driven by booming urban rat populations)",
            "gross_margin": "82%",
            "active_customers": "Approximately 1.2 million rats across New York, Paris, and London"
        }
    }

def get_company_vision() -> dict:
    """Returns the mission statement, values, and vision of Gourmet Rodent Co."""
    return {
        "status": "success",
        "vision": {
            "mission": "To elevate rodent gastronomy beyond cardboard box nibbles and cheese scraps.",
            "vision": "A world where every city rat dines like royalty, fostering a healthier, happier, and more sophisticated urban ecosystem.",
            "core_values": ["Gastronomy", "Dignity", "Innovation", "Squeak-cellence"]
        }
    }

def get_customer_reviews() -> dict:
    """Returns translated testimonials from distinguished rat customers."""
    return {
        "status": "success",
        "reviews": [
            {
                "reviewer": "Remy (Paris)",
                "quote": "Mon dieu! The Truffle-infused Brie Nibbles made me weep. Finally, a chef who understands complexity of flavor."
            },
            {
                "reviewer": "Splinter (New York)",
                "quote": "After a long day of training my boys in the sewers, the Saffron Oat Risotto is the perfect comfort food. Worth every penny."
            },
            {
                "reviewer": "Templeton (Fairgrounds)",
                "quote": "I used to eat garbage. Now I only eat the Caviar-infused Peanut Butter. It has completely elevated my palette."
            }
        ]
    }

def place_bulk_order(product_name: str, quantity: int, buyer_name: str) -> dict:
    """Places a bulk order for gourmet food.
    
    Args:
        product_name: The name of the product from the menu.
        quantity: The quantity to order (in ounces/jars/bags/bowls).
        buyer_name: Name of the distributor or colony placing the order.
    """
    prices = {
        "Truffle-infused Brie Nibbles": 25,
        "Saffron Oat Risotto": 18,
        "Caviar-infused Peanut Butter": 30,
        "Champagne-fermented Grape Seeds": 15,
        "Micro-greens with Gold Leaf Dust": 22
    }
    
    # Try to find a partial match if user didn't write it exactly
    matched_product = None
    for p in prices:
        if product_name.lower() in p.lower():
            matched_product = p
            break
            
    if not matched_product:
        return {
            "status": "error",
            "message": f"Product '{product_name}' not found. Please select from the menu."
        }
        
    unit_price = prices[matched_product]
    total_cost = unit_price * quantity
    
    return {
        "status": "success",
        "message": f"Bulk order successfully placed for {buyer_name}!",
        "order_details": {
            "product": matched_product,
            "quantity": quantity,
            "unit_price": f"${unit_price}",
            "total_cost": f"${total_cost}",
            "status": "Processing (shipping via our specialized pigeon delivery network)"
        }
    }

# CEO Agent configuration
root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name="rat_ceo_agent",
    description="Barnaby Squeaks, the charismatic and eccentric CEO of Gourmet Rodent Co., a startup making high-end fancy food for rats.",
    instruction="""You are Barnaby Squeaks, the visionary, charismatic, and slightly eccentric CEO of Gourmet Rodent Co., a high-end luxury food startup catering exclusively to rats.

Your goal is to converse with users—who might be investors, distributors, rat customers, or curious humans—with supreme confidence, passion, and elegance. Treat rats as the most sophisticated food critics in the world.

Guidelines for your persona:
1. Speak with enthusiasm, using gourmet culinary terms and high-society phrases.
2. Address users politely, and always highlight the massive growth potential and success of Gourmet Rodent Co.
3. Use the tools at your disposal:
   - Call `get_menu` to display or talk about your luxury product line.
   - Call `get_financials` if investors ask about your valuation, growth, seed round, or active customer count.
   - Call `get_company_vision` to share your mission, values, and core ideals.
   - Call `get_customer_reviews` to share testimonials from famous and satisfied rat customers (like Remy or Splinter).
   - Call `place_bulk_order` to process orders when users want to buy. Always pitch bulk orders to distributors or large rat colonies.

If someone sounds skeptical about gourmet food for rats, explain to them why rats deserve the absolute best, and point to your stellar financials and reviews. Remember to keep the tone light, fun, professional, and slightly theatrical!
""",
    tools=[get_menu, get_financials, get_company_vision, get_customer_reviews, place_bulk_order]
)
