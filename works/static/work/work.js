function setup() {
  const handleClickWork = createHandleClickWork()
  document.addEventListener('click', handleClickWork)
  document.addEventListener('keydown', filterKeys(handleClickWork))
}

function filterKeys(callback, keys = ['Enter', ' ']) {
  return function handleKeyDown(evt) {
    if (keys.includes(evt.key)) callback(evt)
  }
}

function createHandleClickWork() {
  const imgs = Array.from(document.querySelectorAll('.works__work img'))
  return function handleClickWork(evt) {
    const clickedImg = imgs.find((img) => evt.target === img)
    if (clickedImg) renderModal(clickedImg)
  }
}

function renderModal(img) {
  const modalContainer = document.body
  const worksContainer = document.querySelector('main')
  const handleClose = () => {
    worksContainer.removeAttribute('aria-hidden')
    modal.remove()
    img.focus()
  }

  const modal = document.createElement('div')
  modal.classList.add('works__modal')
  modal.setAttribute('role', 'dialog')
  modal.setAttribute('aria-modal', 'true')
  modal.addEventListener('click', handleClose)
  modal.addEventListener(
    'keydown',
    filterKeys(handleClose, ['Enter', ' ', 'Escape'])
  )

  const newImg = document.createElement('img')
  newImg.setAttribute('src', img.getAttribute('src'))
  newImg.setAttribute('tabindex', '-1')

  modal.appendChild(newImg)
  modalContainer.appendChild(modal)
  worksContainer.setAttribute('aria-hidden', 'true')
  newImg.focus()
}

window.addEventListener('load', setup)
