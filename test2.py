for message in self.consumer:
    thread = threading.Thread(target=self.deal, args=(message,))
    # thread.setDaemon(True) # 主线程结束, 子线程也会结束
    thread.start()
    thread.join()