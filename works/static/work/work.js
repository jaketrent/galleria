function setup() {
  const handleClickWork = createHandleClickWork()
  document.addEventListener('click', handleClickWork)
  document.addEventListener('keydown', filterKeys(handleClickWork))

  const slideshow = document.querySelector('.collection_slideshow')
  slideshow.addEventListener('click', handleSlideshowClick)
  slideshow.addEventListener('keydown', filterKeys(handleSlideshowClick))

  bindImageHandler()
  bindNextHandler()
  bindPrevHandler()
  bindPlayHandler()
  bindFullscreenHandler()
}

function handleSlideshowClick() {
  renderModal(queryImgs()[0])
  play()
}

function filterKeys(callback, keys = ['Enter', ' ']) {
  return function handleKeyDown(evt) {
    if (keys.includes(evt.key)) callback(evt)
  }
}

function createHandleClickWork() {
  const imgs = queryImgs()
  return function handleClickWork(evt) {
    const clickedImg = imgs.find((img) => evt.target === img)
    if (clickedImg) renderModal(clickedImg)
  }
}

function queryImgs() {
  return Array.from(document.querySelectorAll('.works__work img'))
}

function handleNext(evt) {
  if (interactivePredicate(evt)) {
    renderNext()
  }
}

function renderNext() {
  const imgs = queryImgs()
  const modalImg = document.querySelector('.works__modal img')
  const currentWorkIndex = imgs.findIndex(
    (workImg) => workImg.getAttribute('src') === modalImg.getAttribute('src')
  )
  if (currentWorkIndex + 1 < imgs.length) {
    modalImg.setAttribute('src', imgs[currentWorkIndex + 1].getAttribute('src'))
    return true
  } else {
    return false
  }
}

function handlePrev(evt) {
  if (interactivePredicate(evt)) {
    const imgs = queryImgs()
    const modalImg = document.querySelector('.works__modal img')
    const currentWorkIndex = imgs.findIndex(
      (workImg) => workImg.getAttribute('src') === modalImg.getAttribute('src')
    )
    if (currentWorkIndex - 1 >= 0) {
      modalImg.setAttribute(
        'src',
        imgs[currentWorkIndex - 1].getAttribute('src')
      )
    }
  }
}

function handlePlay(evt) {
  if (interactivePredicate(evt)) {
    play()
  }
}

let playing = false
let playTimer
function play() {
  clearInterval(playTimer)
  playing = !playing

  const playButton = document.querySelector('.works__modal__play')
  playButton.classList.toggle('works__modal__play--paused', !playing)

  if (playing) {
    playTimer = setInterval(() => {
      const renderedNext = renderNext()
      if (!renderedNext) {
        pause()
      }
    }, 2500)
  } else {
    clearInterval(playTimer)
  }
}

function pause() {
  const playButton = document.querySelector('.works__modal__play')
  clearInterval(playTimer)
  playing = false
  playButton.classList.add('works__modal__play--paused', false)
}

function handleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen()
  } else {
    if (document.exitFullscreen) document.exitFullscreen()
  }
}

function bindImageHandler() {
  const modalImg = document.querySelector('.works__modal img')
  bindFresh(modalImg, handleNext)
}

function bindNextHandler() {
  const nextButton = document.querySelector('.works__modal__next')
  bindFresh(nextButton, handleNext)
}

function bindPrevHandler() {
  const prevButton = document.querySelector('.works__modal__prev')
  bindFresh(prevButton, handlePrev)
}

function bindPlayHandler() {
  const playButton = document.querySelector('.works__modal__play')
  bindFresh(playButton, handlePlay)
}

function bindFullscreenHandler() {
  const prevButton = document.querySelector('.works__modal__fullscreen')
  bindFresh(prevButton, handleFullscreen)
}

function bindCloseHandler(img) {
  const modal = document.querySelector('.works__modal')
  const close = modal.querySelector('.works__modal__close')
  const worksContainer = document.querySelector('main')

  const hideModal = () => {
    if (document.fullscreenElement && document.exitFullscreen)
      document.exitFullscreen()
    pause()
    modal.classList.add('works__modal--hidden')
    modal.setAttribute('aria-hidden', 'true')
    worksContainer.removeAttribute('aria-hidden')
    img.focus()
  }

  const handleClose = (evt) => {
    if (interactivePredicate(evt)) hideModal()
  }

  const handleEscape = (evt) => {
    if (evt.key === 'Escape') hideModal()
  }

  bindFresh(close, handleClose)
  bindFresh(modal, handleEscape)

  modal.removeEventListener('keydown', handleEscape)
  modal.addEventListener('keydown', handleEscape)
}

function interactivePredicate(evt) {
  return (
    evt.type === 'click' ||
    (evt.type === 'keydown' && ['Enter', ' '].includes(evt.key))
  )
}

function bindFresh(el, callback) {
  el.removeEventListener('click', callback)
  el.removeEventListener('keydown', callback)
  el.addEventListener('click', callback)
  el.addEventListener('keydown', callback)
}

function setModalImgFrom(img) {
  const modalImg = document.querySelector('.works__modal img')
  modalImg.setAttribute('src', img.getAttribute('src'))
  return modalImg
}

function showModal() {
  const modal = document.querySelector('.works__modal')
  modal.classList.remove('works__modal--hidden')
}

function hideOtherWorks() {
  const worksContainer = document.querySelector('main')
  worksContainer.setAttribute('aria-hidden', 'true')
}

function focusModalImage() {
  const modalImg = document.querySelector('.works__modal img')
  modalImg.focus()
}

function renderModal(img) {
  setModalImgFrom(img)
  bindCloseHandler(img)
  showModal()
  focusModalImage()
}

window.addEventListener('load', setup)
