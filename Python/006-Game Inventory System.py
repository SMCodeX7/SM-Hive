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
            if not game_inventory_system.inventory:
                return "Inventory Is Empty"
            
            formatted_items = []

            for index,item in enumerate(game_inventory_system.inventory,start=1):
                name = item["name"]
                rarity = item["rarity"]
                value = item["value"]

                formatted_string = f"{index}. {name} ({rarity}) - ${value}"
                formatted_items.append(formatted_string)
            return "\n".join(formatted_items)
        
        case "add":
            if not new_items:
                return "No Items To Add"

            added_names = []

            for item_name in new_items:
                item_data = {
                    "name" : item_name,
                    "rarity" : merged_props["rarity"],
                    "value" : merged_props["value"],
                    "durability" : merged_props["durability"],
                    "cateogry" : merged_props["category"]
                }   

                game_inventory_system.inventory.append(item_data)
                added_names.append(item_name)
            return f"Added : {', '.join(added_names)}"
        
        case "search":
            search_term = item_properties.get("name","")

            if not search_term:
                return "Please Provide A Search Term"
            
            search_term = search_term.lower()

            found_items = []

            for item in game_inventory_system.inventory:
                item_name_lower = item["name"].lower()
                item_category_lower = item["category"].lower()

                if search_term in item_name_lower or search_term in item_category_lower:
                    found_items.append(item)

            if not found_items:
                return "No Items Found"
            else:
                found_names = [item["name"]for item in found_items]
                item_count = len(found_items)
                names_string = ", ".join(found_names)

            return f"Found {item_count} item(s): {names_string}"
        
        case "use":
            item_name = item_properties.get("name","")

            if not item_name:
                return "Please Specify Item Name"

            item_found = None
            item_index = -1

            for i,item in enumerate(game_inventory_system.inventory):
                if item_name == item["name"]:
                    item_found = item
                    item_index = i
                    break

            if item_found is None:
                    return f"{item_name} Not In Inventory"

            damage_amount = item_properties.get("damage",10)

            current_durability = item_found["durability"]
            new_durability = current_durability - damage_amount

            if new_durability <= 0:
                game_inventory_system.inventory.pop(item_index)
                return f"Used Item {item_name}. It Broke"
            else:
                item_found["durability"] = new_durability
                return f"Used {item_name}. Durability: {new_durability}"

        case _:
            return "none"
