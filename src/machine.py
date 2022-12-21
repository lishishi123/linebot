from src.fsm import TocMachine # import trick

def create_machine():
    machine = TocMachine(
        states=["user", "menu", "introduction", "show_fsm_pic", "search_value_now", "value_now",
                "search_value_full", "value_full", "search_fluctuation", "fluctuation"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "show_fsm_pic",
                "conditions": "is_going_to_show_fsm_pic",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "introduction",
                "conditions": "is_going_to_introduction",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_value_now",
                "conditions": "is_going_to_search_value_now",
            },
            {
                "trigger": "advance",
                "source": "search_value_now",
                "dest": "value_now",
                "conditions": "is_going_to_value_now",
            },
            {
                "trigger": "advance",
                "source": "value_now",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_value_full",
                "conditions": "is_going_to_search_value_full",
            },
            {
                "trigger": "advance",
                "source": "search_value_full",
                "dest": "value_full",
                "conditions": "is_going_to_value_full",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_fluctuation",
                "conditions": "is_going_to_search_fluctuation",
            },
            {
                "trigger": "advance",
                "source": "search_fluctuation",
                "dest": "fluctuation",
                "conditions": "is_going_to_fluctuation",
            },
            {
                "trigger": "advance",
                "source": "value_now",
                "dest": "search_value_full",
                "conditions": "is_going_to_search_value_full",
            },
            {"trigger": "go_back", "source": ["introduction", "show_fsm_pic", "value_full", "fluctuation"],
             "dest": "menu"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine


# create_machine().get_graph().draw("fsm.png", prog="dot")
