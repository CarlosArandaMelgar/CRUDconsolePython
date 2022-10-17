import logging as log

log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel Debug')
    log.info('Mensaje a nivel Info')
    log.warning('Mensaje a nivel Warning')
    log.error('Msj a nivel error')
    log.critical('Msj a nivel crítico')
