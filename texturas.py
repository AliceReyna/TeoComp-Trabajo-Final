screen.blit(background_image, (0, 0))

        if powerup:
            powerup.draw(screen)
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        LAST_PLATFORM_IMAGE = pygame.image.load("square/imagen_last_platform.png")  # Reemplaza "ruta/imagen_last_platform.png" con la ruta de tu imagen
        PLATFORM_IMAGE = pygame.image.load("square/imagen_platform.png")  # Reemplaza "ruta/imagen_platform.png" con la ruta de tu imagen


        for i, platform in enumerate(platforms):
            if i == len(platforms) - 1:  # Si es la última plataforma
                image = LAST_PLATFORM_IMAGE
            else:
                image = PLATFORM_IMAGE
                
            # Dibuja la imagen en lugar del rectángulo de color
            screen.blit(image, (platform[0], platform[1]))
