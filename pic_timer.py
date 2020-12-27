
def TMR0():
    """
    TMR = Resolution - (( T * Fosc ) / (4 * Prescale))


    ### tmr0 ve tmr0L, tmr0H gibi değerleri bulmanın bir diğer yöntemi
    INF:
        - tmr0 8 bit genişliğindeo yüzden direk olarak 2**8 = 256 değerini alabilirim, pres değerine gerek yok
        - tmr0H ve tmr0L:
            istenen delay: 3ms
            XTAL = 4 MHz
            Fins = XTaL / 4 = 1 MHz
            Tins = 1 / Fins = 1 us
            Timer Count = istenen delay / Tins = 3ms/1us = 3000


            initial values for timer =  (max count) - count + 1
                                        65535 - 3000 + 1 65536
                                    hex:0xFFFF - 0xBB8 + 1 = 0xF448
                                    tmr0L = 0xF4
                                    tmr0H = 0x48

    """



    # get values
    res = int(input('(Resolution) The max value of the timer: '))
    T = float(input('(T) Delay Time in Second: '))
    Fosc = int(input('(Fosc) The oscillator freq (MHZ): '))
    #pres = int(input('(Prescale) The max prescale value: '))
    pres = 2**8


    # delay calculation


   # calculate and print
    ret = res - ((T * (Fosc*(10**6))) / (4 * pres))
    num = round(ret)
    hex_ = hex(num)
    print(f"""
        Decimal: {num} H,
        Hexadecimal: {hex_} H
        """)


def internal_inst_cycle():
    """
    Internal instruction cycle = 1 / [(Processor Frequency) / 4] = 1 / (8 MHz / 4) = 500nS
    TMR0 overflow = Internal instruction cycle x 28 (we must count the zero) = 500nS x 256 = 128μS
    """

    # clock cycle
    freg = int(input('Processor Frequency: '))
    cycle = (1 / ((freg / 4)))*1000

    # tmr0 overflow
    # NOTE: tmr0 is 8-bit wide
    # this why we multiply it with 2**8
    # cycle as ns
    # so tmr0 as us
    tmr0_overflow = cycle * (2**8)

    # print clock cycle
    # to convert to ns
    print(f'Cycle: {cycle} ns')
    print(f'timer0 overflow: {tmr0_overflow} us')


if __name__ == '__main__':
    print("""
        1: TMR HESAPLA

    """)
    option = int(input('~# :: '))
    if option == 1:
        TMR0()
    elif option == 2:
        internal_inst_cycle()
    else: 
        print('aralıkta bir değer girin !!')

