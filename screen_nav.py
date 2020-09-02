screen_helper = """

ScreenManager:
    MenuScreen:
    CanapeScreen:
    BasketScreen:


<MDRaisedButton>:
    font_size: '20sp'

<MenuButton@Button>:
    font_size: '15sp'



<MenuScreen>:
    name: 'menu'
    BoxLayout:    
        padding: 20
        orientation: 'vertical'

        AnchorLayout:
            size_hint: 1.0, 0.1
    
            Label:                 
                text: 'PETROV FOOD'
    
    
        BoxLayout:
    
        GridLayout:
            cols: 2
            orientation: 'horizontal'
    
            Button:
                name: 'canape'
                text: 'Канапе'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'canape'
    
            Button:
                text: 'Брускетты'
    
            Button:
                text: 'Блины'
    
            Button:
                text: 'Холодные закуски'
    
            Button:
                text: 'Салаты'
    
            Button:
                text: 'Тарталетки'
    
            Button:
                text: 'Наборы'
    
            Button:
                text: 'КОРЗИНА'
                on_press:
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'basket'

<CanapeScreen>
    name: 'canape'
    ScrollView:         
        bar_width: 1
        bar_color: [0, 123, 199, 1]               
        GridLayout:
            name: 'canape_scroll'            
            size_hint_y: 1.2                                         
            cols: 2
            padding: 20                   
            
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'   
                                     
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'
                    
            Button:
                text: 'Back to menu'
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'menu'                                


<BasketScreen>
    name: 'basket'
    BoxLayout:
        Button:
            text: 'Back to menu'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
"""
