import sys

def shrink(s: str) -> None:
    """แสดง 8 ตัวอักษรแรกของสตริง"""
    print(s[:8])

def enlarge(s: str) -> None:
    """เติม 'Z' ต่อท้ายให้ยาวรวมเป็น 8 ตัวอักษร แล้วแสดงผล"""
    print(s + 'Z' * (8 - len(s)))

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:           
            print(arg)