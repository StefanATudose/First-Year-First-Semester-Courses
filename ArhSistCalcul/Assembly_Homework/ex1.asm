.data
	sirhexa: .space 101
	formatScanf: .asciz "%[^\n]s"
	formatPrintfvar: .asciz "%c "
	formatPrintoper: .asciz "%s "
	formatPrintnr: .asciz "%d "
	formatPrintneg: .asciz "-%d "
	formatPrintenter: .asciz "\n"
	trei: .long 3
	identifcurent: .space 4
	valcurenta: .space 4
	operlet: .asciz "let"
	operadd: .asciz "add"
	opersub: .asciz "sub"
	opermul: .asciz "mul"
	operdiv: .asciz "div"
.text

.global main

main:
	push $sirhexa
	push $formatScanf
	call scanf
	popl %ebx
	popl %ebx

	movl $sirhexa, %edi
	xor %ecx, %ecx
	
et_for:	
	movb (%edi, %ecx, 1), %al
	cmp $0, %al
	je exit
	
	;//impart %ecx la 3, daca are rest 0, atunci merg in identificare, daca are rest 1 sau 2, merg in calculare valoare
	pushl %eax
	movl %ecx, %eax
	xor %edx, %edx
	divl trei
	popl %eax
	cmp $0, %edx
	je identificator
	
	jmp indecimal
	
increment_for:
	incl %ecx
	jmp et_for
	
identificator:
	cmp $56, %al
	je nrpozitiv
	cmp $57, %al
	je nrnegativ
	cmp $65, %al
	je variablia
	cmp $67, %al
	je operatie

nrpozitiv:
	movl $0, identifcurent
	jmp increment_for

nrnegativ:
	movl $1, identifcurent
	jmp increment_for
	
variablia:
	movl $2, identifcurent
	jmp increment_for
	
operatie:
	movl $3, identifcurent
	jmp increment_for

indecimal:
	cmp $48, %al
	je cif0
	cmp $49, %al
	je cif1
	cmp $50, %al
	je cif2
	cmp $51, %al
	je cif3
	cmp $52, %al
	je cif4
	cmp $53, %al
	je cif5
	cmp $54, %al
	je cif6
	cmp $55, %al
	je cif7
	cmp $56, %al
	je cif8
	cmp $57, %al
	je cif9
	cmp $65, %al
	je cif10
	cmp $66, %al
	je cif11
	cmp $67, %al
	je cif12
	cmp $68, %al
	je cif13
	cmp $69, %al
	je cif14
	cmp $70, %al
	je cif15

cif0:
	cmp $1, %edx
	je cif0doi
	cmp $2, %edx
	je cif0trei

cif1:
	cmp $1, %edx
	je cif1doi
	cmp $2, %edx
	je cif1trei	

cif2:
	cmp $1, %edx
	je cif2doi
	cmp $2, %edx
	je cif2trei
cif3:
	cmp $1, %edx
	je cif3doi
	cmp $2, %edx
	je cif3trei
cif4:
	cmp $1, %edx
	je cif4doi
	cmp $2, %edx
	je cif4trei
cif5:
	cmp $1, %edx
	je cif5doi
	cmp $2, %edx
	je cif5trei
cif6:
	cmp $1, %edx
	je cif6doi
	cmp $2, %edx
	je cif6trei
cif7:
	cmp $1, %edx
	je cif7doi
	cmp $2, %edx
	je cif7trei
cif8:
	cmp $1, %edx
	je cif8doi
	cmp $2, %edx
	je cif8trei
cif9:
	cmp $1, %edx
	je cif9doi
	cmp $2, %edx
	je cif9trei
cif10:
	cmp $1, %edx
	je cif10doi
	cmp $2, %edx
	je cif10trei
cif11:
	cmp $1, %edx
	je cif11doi
	cmp $2, %edx
	je cif11trei
cif12:
	cmp $1, %edx
	je cif12doi
	cmp $2, %edx
	je cif12trei
cif13:
	cmp $1, %edx
	je cif13doi
	cmp $2, %edx
	je cif13trei
cif14:
	cmp $1, %edx
	je cif14doi
	cmp $2, %edx
	je cif14trei
cif15:
	cmp $1, %edx
	je cif15doi
	cmp $2, %edx
	je cif15trei
	
cif0doi:
	pushl %eax
	movl $0, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif0trei:
	add $0, valcurenta
	jmp afisare
	
cif7doi:
	pushl %eax
	movl $7, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif7trei:
	add $7, valcurenta
	jmp afisare
	
cif1doi:
	pushl %eax
	movl $1, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif1trei:
	add $1, valcurenta
	jmp afisare
	
cif2doi:
	pushl %eax
	movl $2, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif2trei:
	add $2, valcurenta
	jmp afisare
	
cif3doi:
	pushl %eax
	movl $3, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif3trei:
	add $3, valcurenta
	jmp afisare
	
cif4doi:
	pushl %eax
	movl $4, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif4trei:
	add $4, valcurenta
	jmp afisare
	
cif5doi:
	pushl %eax
	movl $5, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif5trei:
	add $5, valcurenta
	jmp afisare
	
cif6doi:
	pushl %eax
	movl $6, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif6trei:
	add $6, valcurenta
	jmp afisare
	
cif8doi:
	pushl %eax
	movl $8, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif8trei:
	add $8, valcurenta
	jmp afisare
	
cif9doi:
	pushl %eax
	movl $9, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif9trei:
	add $9, valcurenta
	jmp afisare
	
cif10doi:
	pushl %eax
	movl $10, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif10trei:
	add $10, valcurenta
	jmp afisare
	
cif11doi:
	pushl %eax
	movl $11, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif11trei:
	add $11, valcurenta
	jmp afisare
	
cif12doi:
	pushl %eax
	movl $12, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif12trei:
	add $12, valcurenta
	jmp afisare
	
cif13doi:
	pushl %eax
	movl $13, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif13trei:
	add $13, valcurenta
	jmp afisare
	
cif14doi:
	pushl %eax
	movl $14, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif14trei:
	add $14, valcurenta
	jmp afisare
	
cif15doi:
	pushl %eax
	movl $15, %eax
	movl $16, %ebx
	mull %ebx
	movl %eax, valcurenta
	popl %eax
	jmp increment_for
	
cif15trei:
	add $15, valcurenta
	jmp afisare
	
	
afisare:
	cmp $0, identifcurent
	je afisarepozitiv
	cmp $1, identifcurent
	je afisarenegativ
	cmp $2, identifcurent
	je afisarevariabila
	cmp $3, identifcurent
	je afisareoperatie	
	
afisarepozitiv:
	pushl %ecx
	
	pushl valcurenta
	pushl $formatPrintnr
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	jmp increment_for
	
afisarenegativ:
	pushl %ecx
	
	pushl valcurenta
	pushl $formatPrintneg
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	jmp increment_for

afisarevariabila:
	pushl %ecx
	
	pushl valcurenta
	pushl $formatPrintfvar
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for

afisareoperatie:
	cmp $0, valcurenta
	je afislet
	cmp $1, valcurenta
	je afisadd
	cmp $2, valcurenta
	je afissub
	cmp $3, valcurenta
	je afismul
	cmp $4, valcurenta
	je afisdiv
	
afislet:
	pushl %ecx
	
	pushl $operlet
	pushl $formatPrintoper
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for

afisadd:
	pushl %ecx
	
	pushl $operadd
	pushl $formatPrintoper
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for

afissub:
	pushl %ecx
	
	pushl $opersub
	pushl $formatPrintoper
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for

afismul:
	pushl %ecx
	
	pushl $opermul
	pushl $formatPrintoper
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for

afisdiv:
	pushl %ecx
	
	pushl $operdiv
	pushl $formatPrintoper
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	
	popl %ecx
	
	jmp increment_for


exit:	
	pushl $formatPrintenter
	call printf
	popl %ebx
	mov $1, %eax
	xor %ebx, %ebx
	int $0x80 

