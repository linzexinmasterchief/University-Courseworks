def add_hover_effect_to_widget(widget, hover_color = '#ffffff', original_color = '#eeeeee'):
    def on_enter(e):
        widget['background'] = hover_color
    def on_leave(e):
        widget['background'] = original_color
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)