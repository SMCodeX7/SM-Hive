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
        
        case "sort":
            sort_by = item_properties.get("by","name")
            reverse_order = item_properties.get("reverse",False)

            if sort_by == "name":
                game_inventory_system.inventory.sort(key=lambda item:item["name"],reverse=reverse_order)
            elif sort_by == "value":
                game_inventory_system.inventory.sort(key=lambda item:item["value"],reverse=reverse_order)
            elif sort_by == "rarity":
                rarity_rank = {
                    "common" : 1,
                    "uncommon" : 2,
                    "rare" : 3,
                    "epic" : 4,
                    "legendary" : 5
                }
                game_inventory_system.inventory.sort(key=lambda item:rarity_rank.get(item["rarity"],0),reverse=reverse_order)

            else:
                print("Error. Unknown Sort Method")

            return f"Inventory sorted by {sort_by}" + (" (descending)" if reverse_order else "")

        case "stats":
            if not game_inventory_system.inventory:
                return "Inventory Is Empty. No Statistics To Show"

            total_items = len(game_inventory_system.inventory)
            total_value = sum(item["value"] for item in game_inventory_system.inventory)
            total_durability = sum(item["durability"] for item in game_inventory_system.inventory)
            average_durability = total_durability / total_items
            
            all_rarities = [item["rarity"] for item in game_inventory_system.inventory]
            rarity_counts = {}
            for rarity in all_rarities:
                if rarity in rarity_counts:
                    rarity_counts[rarity] += 1
                else:
                    rarity_counts[rarity] = 1

            most_valuable = None
            highest_value = 0

            for item in game_inventory_system.inventory:
                if item["value"] > highest_value:
                    highest_value = item["value"]
                    most_valuable = item["name"]
            
            result = f"""
                📊 INVENTORY STATISTICS
                Total Items: {total_items}
                Total Value: ${total_value}
                Average Durability: {average_durability:.1f}

                Rarity Distribution:"""

            for rarity, count in rarity_counts.items():
                    result += f"\n  {rarity.title()}: {count}"

            result += f"\n\nMost Valuable: {most_valuable} (${highest_value})"

            return result

        case _:
            return "none"
