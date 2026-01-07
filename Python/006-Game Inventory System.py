def game_inventory_system(*new_items, action="show", **item_properties):
    if not hasattr(game_inventory_system,"inventory"):
        game_inventory_system.inventory = []
    
    default_props = { 
        "rarity" : "common",
        "value" : 10,
        "durability" : 100,
        "category" : "misc"
    }
    
    merged_props = {**default_props, **item_properties}
    
    match action:
        case "show":
            return "Showing Inventory"
        case "add":
            return "add"
        case _:
            return "none"

print(game_inventory_system(action="delete"))
