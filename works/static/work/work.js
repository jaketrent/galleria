function setup() {
  const handleClickWork = createHandleClickWork()
  document.addEventListener('click', handleClickWork)
  document.addEventListener('keydown', filterKeys(handleClickWork))

  bindImageHandler()
  bindNextHandler()
  bindPrevHandler()
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
    const imgs = queryImgs()
    const modalImg = document.querySelector('.works__modal img')
    const currentWorkIndex = imgs.findIndex(
      (workImg) => workImg.getAttribute('src') === modalImg.getAttribute('src')
    )
    if (currentWorkIndex + 1 < imgs.length) {
      modalImg.setAttribute(
        'src',
        imgs[currentWorkIndex + 1].getAttribute('src')
      )
    }
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

function bindCloseHandler(img) {
  const modal = document.querySelector('.works__modal')
  const close = modal.querySelector('.works__modal__close')
  const worksContainer = document.querySelector('main')

  const hideModal = () => {
    worksContainer.removeAttribute('aria-hidden')
    modal.classList.add('works__modal--hidden')
    modal.setAttribute('aria-hidden', 'true')
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
