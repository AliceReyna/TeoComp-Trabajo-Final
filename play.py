def play():
    while True:
        PLAY_BALL = Button(game_loop())
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        #PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        #PLAY_RECT = PLAY_BALL.get_rect(center=(200, 400))
        SCREEN.blit(PLAY_BALL)

        #Button BACK
        PLAY_BACK = Button(image=None, pos=(800, 800), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
