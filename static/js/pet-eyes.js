const eyes = document.querySelectorAll('.eye');

document.addEventListener('mousemove', (e) => {
  eyes.forEach(eye => {
    const pupil = eye.querySelector('.pupil');
    const rect = eye.getBoundingClientRect();

    // центр глаза
    const eyeCenterX = rect.left + rect.width / 2;
    const eyeCenterY = rect.top + rect.height / 2;

    // вектор к мышке
    let dx = e.clientX - eyeCenterX;
    let dy = e.clientY - eyeCenterY;

    // ограничиваем смещение зрачка
    const maxDist = rect.width / 4;
    const distance = Math.sqrt(dx*dx + dy*dy);
    if (distance > maxDist) {
      const angle = Math.atan2(dy, dx);
      dx = Math.cos(angle) * maxDist;
      dy = Math.sin(angle) * maxDist;
    }

    pupil.style.transform = `translate(${dx}px, ${dy}px)`;
  });
});