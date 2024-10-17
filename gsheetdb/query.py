from typing import Dict, List, Any

def apply_filters(data: List[Dict], query: Dict) -> List[Dict]:
    """Apply query filters to the data."""
    def match(item, query):
        for key, condition in query.items():
            if isinstance(condition, dict):
                for op, value in condition.items():
                    if not eval_operator(op, item.get(key), value):
                        return False
            elif item.get(key) != condition:
                return False
        return True
    return [item for item in data if match(item, query)]

def eval_operator(op: str, item_value: Any, condition_value: Any) -> bool:
    """Evaluate query operators."""
    operators = {
        "$eq": lambda x, y: x == y,
        "$gt": lambda x, y: x > y,
        "$lt": lambda x, y: x < y,
        "$in": lambda x, y: x in y,
        "$nin": lambda x, y: x not in y,
    }
    return operators[op](item_value, condition_value)
