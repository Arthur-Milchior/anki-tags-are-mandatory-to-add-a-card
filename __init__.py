from aqt import gui_hooks

def reject_empty_tag(problem, note):
    if not any(note.tags):
        return "Please add a tag"
    else:
        return problem

gui_hooks.add_cards_will_add_note.append(reject_empty_tag)
