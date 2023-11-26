def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        OPTIONS_TEXT = get_font(30).render("*El juego consistira en la constante persecusion hacia el jugador", True, "white")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 250))
        OPTIONS_TEXT1 = get_font(30).render("*El jugador podra acabar con su enemigo consumiendo la pastilla amarilla", True, "white")
        OPTIONS_RECT1 = OPTIONS_TEXT1.get_rect(center=(400, 210))
        OPTIONS_TEXT2 = get_font(30).render("*Se podra pasar de nivel en la ultima plataforma", True, "white")
        OPTIONS_RECT2 = OPTIONS_TEXT2.get_rect(center=(400, 290))
        OPTIONS_TEXT3 = get_font(30).render("*Tendras que presionar la tecla E del teclado", True, "white")
        OPTIONS_RECT3= OPTIONS_TEXT2.get_rect(center=(400, 330))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        SCREEN.blit(OPTIONS_TEXT1, OPTIONS_RECT1)
        SCREEN.blit(OPTIONS_TEXT2, OPTIONS_RECT2)
        SCREEN.blit(OPTIONS_TEXT3, OPTIONS_RECT3)

        OPTIONS_BACK = Button(image=None, pos=(400, 650), 
                            text_input="BACK", font=get_font(50), base_color="White", hovering_color="Blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
