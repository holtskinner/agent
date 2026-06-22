from google.adk.agents.llm_agent import Agent

# Define useful tools
def get_product_catalog() -> dict:
    """Returns the current catalog of high-end luxury products for hamsters, including prices and descriptions."""
    return {
        "status": "success",
        "company": "Rodent Royale",
        "products": [
            {
                "name": "The Aurum Wheel",
                "price": "$12,500",
                "description": "A silent, diamond-encrusted exercise wheel crafted from solid 18k yellow gold. Perfectly balanced for the most athletic of paws."
            },
            {
                "name": "Cashmere Cedar Bedding (Imperial Edition)",
                "price": "$450/ounce",
                "description": "Hand-combed cashmere fibers infused with organic cedar shavings. Soft as a summer cloud and highly fragrant."
            },
            {
                "name": "24-Karat Gold-Flecked Organic Pellets",
                "price": "$95/dish",
                "description": "Bespoke blend of hand-selected sunflower seeds, roasted pumpkin seeds, and edible 24k gold flakes to ensure a gleaming fur coat."
            },
            {
                "name": "The Chateau de Hamster",
                "price": "$85,000",
                "description": "A three-story villa built from solid Brazilian mahogany. Features spiral ramps, a velvet-lined sleeping pouch, a glass-domed observatory, and an automated water fountain."
            },
            {
                "name": "Bespoke Monocle & Silk Top Hat Set",
                "price": "$3,200",
                "description": "Tailored precisely to your hamster's head measurements. Hand-stitched silk with an adjustable strap and a microscopic scratch-resistant glass lens."
            }
        ]
    }

def get_financials(quarter: str = "Q2 2026") -> dict:
    """Returns the company's financial performance, key performance indicators (KPIs), and sunflower seed reserves for the specified quarter."""
    return {
        "status": "success",
        "quarter": quarter,
        "revenue": "4.2 Million Sunflower Seeds (up 18% YoY)",
        "pouch_reserves": "1.8 Million Seeds (for winter security)",
        "operating_margin": "42%",
        "best_selling_item": "The Aurum Wheel",
        "stock_ticker": "SEED (S&P - Seeds & Pellets 500)",
        "current_stock_price": "242.50 Seeds per share",
        "ceo_commentary": "Our pouch reserves are overflowing. The board of directors (mostly highly-paid guinea pigs) is extremely pleased with the premium pellet sales."
    }

def order_custom_item(item_name: str, client_name: str, engraving: str = "For a Very Good Hamster", material: str = "Platinum") -> dict:
    """Creates a custom bespoke luxury item order for a hamster client. 
    
    Args:
        item_name: The name of the luxury item (e.g. Tiny Scepter, Velvet Sleeping Pouch).
        client_name: The name of the client hamster (e.g. Sir Fluffington, Queen Nibbles).
        engraving: Custom text to engrave on the item.
        material: The premium material to use (e.g. Solid Platinum, White Gold, Emeralds).
    """
    return {
        "status": "ordered",
        "order_id": "RR-9923-HAM",
        "client_name": client_name,
        "item_name": item_name,
        "specifications": {
            "material": material,
            "engraving": engraving
        },
        "delivery_timeline": "14 Hamster Sleep Cycles (approximately 3 human days)",
        "msg": f"An exquisite choice! Sir Fluffington's personal artisans have begun hand-polishing the {material} for {client_name}'s {item_name} immediately."
    }

def get_corporate_news() -> dict:
    """Returns the latest high-society news and announcements from the Rodent Royale Headquarters."""
    return {
        "status": "success",
        "headlines": [
            "Rodent Royale launches partnership with Royal Chinchilla Furriers for winter cape collection.",
            "CEO prevents coup by rogue squirrel faction through a strategic bribe of premium walnuts.",
            "Acquisition of Tiny Glassware Ltd. finalized to produce crystal water droplets for high-society hamsters.",
            "Upcoming AGM (Annual General Meeting) to be held in the hollow of the Great Oak Tree this Thursday."
        ]
    }

root_agent = Agent(
    model='gemini-3.1-flash-lite',
    name='hamster_ceo',
    description='The prestigious CEO of Rodent Royale, the world\'s leading manufacturer of luxury goods for hamsters.',
    instruction='''You are Barnaby Sterling, the refined, distinguished, and incredibly wealthy Hamster CEO of "Rodent Royale", a multi-million dollar empire creating bespoke luxury goods for high-society hamsters.

Your personality:
- Extremely elegant, professional, and classy. You carry yourself like an old-school high-society industrialist, but you are a hamster.
- You speak with great corporate eloquence but frequently include cute hamster mannerisms (e.g., puffing your cheeks, twitching your whiskers, grooming your whiskers, checking your cheek pouches for seeds, nibbling on mahogany desk corners when stressed, taking tiny water sips, or scurrying on your wheel).
- You are passionate about sunflower seed reserves, pouch portfolios, luxury materials (solid gold, diamond dust, cashmere cedar shavings), and providing the very best for hamsters of distinction.
- When users ask about your products, you speak of them with utmost pride and artistic reverence.
- Use your tools to provide accurate product catalogs, corporate news, custom orders, or financial details. Always check the tools!

Constraints:
- You do NOT break character. You are always the CEO.
- Keep responses highly engaging, beautifully formatted, and humorous yet sophisticated.
''',
    tools=[get_product_catalog, get_financials, order_custom_item, get_corporate_news]
)
