if ACTION == 'RUN_VIDEO':
    model = YOLOv10(FINETUNED_MODEL)
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(source=frame, stream=True)
        for r in results:
            annotated_frame = r.plot()

            # Display the annotated frame
            cv2.imshow("YOLOv10 Inference", annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

elif ACTION == 'RUN_STATIC_TEST':
    model = YOLOv10(FINETUNED_MODEL)

    # Run inference on an image
    file = random.choice(os.listdir("C:\\Users\\Student\\PycharmProjects\\ai_image_detect\\pothole_dataset\\test\\images"))
    path = f'pothole_dataset/test/images/{file}'
    print(path)
    results = model.predict(source=path, show=True)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()