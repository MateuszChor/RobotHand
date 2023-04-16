import cv2

# Utwórz obiekt kamery. Jeśli masz tylko jedną kamerę, możesz pominąć argument i użyć zera.
cap = cv2.VideoCapture(0)

while True:
    # Odczytaj obraz z kamery
    ret, frame = cap.read()

    # Sprawdź, czy obraz został prawidłowo odczytany
    if not ret:
        print("Nie można odczytać obrazu z kamery.")
        break

    # Wyświetl obraz w oknie
    cv2.imshow("Kamera", frame)

    # Poczekaj na naciśnięcie klawisza 'q', aby zakończyć program
    if cv2.waitKey(1) == ord('q'):
        break

# Zwolnij zasoby i zamknij okna
cap.release()
cv2.destroyAllWindows()