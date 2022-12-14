!************************************************
!* Analytical calculation of choked nozzle flow *
!************************************************
      PROGRAM Choked_Nozzle
      IMPLICIT REAL(8) (A-H,O-Z)

!** Number of cells along the nozzle
      INTEGER, PARAMETER :: Nx=1000

!** Tolerance
      REAL(8), PARAMETER :: TOL=1.d-10

!** Ratio of specific heats
      REAL(8), PARAMETER :: G=1.4d0

      REAL(8), PARAMETER :: Gm1=G-1.d0
      REAL(8), PARAMETER :: Gp1=G+1.d0

      REAL(8), DIMENSION(0:Nx) :: X, Y
      REAL(8), DIMENSION(0:Nx) :: aMd, Pd, Rd, Ud 

!** Nozzle shape
      Area(xx) = 0.5d0+0.5d0*(1.d0-2.d0*xx)**2

!** Gasdynamic function
      Func(aM) = (aMref/aM)*((1.d0+0.5d0*Gm1*aM*aM)/
     &            (1.d0+0.5d0*Gm1*aMref*aMref))
     &            **(0.5d0*Gp1/Gm1)-S/Sref

      DO i=0,Nx
        X(i) = DBLE(i)/Nx
        Y(i) = Area(X(i))
      END DO

      Nth = Nx/2
      Nsh = 3*Nx/4
      Xth = 0.5d0
      Xsh = 0.75d0
      Ath = Area(Xth)
      Ash = Area(Xsh)

      aMref = 1.d0
      Pref = 1.d0
      Rref = 1.d0
      Uref = 1.d0
      Sref = Ath
      S = Ash

      aM1 = 1.d0
      aM2 = 50.d0
      F1 = Func(aM1)
      F2 = Func(aM2)

  10  aM = 0.5d0*(aM1+aM2)
      F = Func(aM)
      IF (aM2-aM1.LE.TOL) GO TO 20 
      IF (F*F1.GE.0.) THEN
        aM1 = aM
        F1 = F
      ELSE
        aM2 = aM
        F2 = F
      END IF
      GO TO 10
  20  CONTINUE

      aMs1 = aM
      aMs2 = SQRT((2.d0+Gm1*aMs1*aMs1)/
     &            (2.d0*G*aMs1*aMs1-Gm1))
      Ps1 = Pref*((1.d0+0.5d0*Gm1*aMref*aMref)/
     &            (1.d0+0.5d0*Gm1*aMs1*aMs1))**(G/Gm1)
      Rs1 = Rref*(Ps1/Pref)**(1.d0/G)
      Us1 = Rref*Uref*Sref/(Rs1*Ash)
      Ps2 = Ps1*(2.d0*G*aMs1*aMs1-Gm1)/Gp1
      Rs2 = Rs1*(Gp1*Ps2+Gm1*Ps1)/(Gm1*Ps2+Gp1*Ps1)
      Us2 = Rs1*Us1/Rs2

      DO i=0,Nth-1
        S = Y(i)
        aM1 = 0.001d0
        aM2 = 1.d0
        F1 = Func(aM1)
        F2 = Func(aM2)
  30    aM = 0.5d0*(aM1+aM2)
        F = Func(aM)
        IF (aM2-aM1.LE.TOL) GO TO 40 
        IF (F*F1.GE.0.) THEN
          aM1 = aM
          F1 = F
        ELSE
          aM2 = aM
          F2 = F
        END IF
        GO TO 30
  40    CONTINUE
        aMd(i) = aM
        Pd(i) = Pref*((1.d0+0.5d0*Gm1*aMref*aMref)/
     &         (1.d0+0.5d0*Gm1*aMd(i)*aMd(i)))**(G/Gm1)
        Rd(i) = Rref*(Pd(i)/Pref)**(1.d0/G)
        Ud(i) = Rref*Uref*Sref/(Rd(i)*S)
      END DO
      AMd(Nth) = 1.d0
      Pd(Nth) = Pref
      Rd(Nth) = Rref
      Ud(Nth) = Uref

      DO i=Nth+1,Nsh-1
        S = Y(i)
        aM1 = 1.d0
        aM2 = aMs1
        F1 = Func(aM1)
        F2 = Func(aM2)

  50    aM = 0.5d0*(aM1+aM2)
        F = Func(aM)
        IF (aM2-aM1.LE.TOL) GO TO 60 
        IF (F*F1.GE.0.) THEN
          aM1 = aM
          F1 = F
        ELSE
          aM2 = aM
          F2 = F
        END IF
        GO TO 50
  60    CONTINUE
        AMd(i) = aM
        Pd(i) = Pref*((1.d0+0.5d0*Gm1*aMref*aMref)/
     &         (1.d0+0.5d0*Gm1*aMd(i)*aMd(i)))**(G/Gm1)
        Rd(i) = Rref*(Pd(i)/Pref)**(1.d0/G)
        Ud(i) = Rref*Uref*Sref/(Rd(i)*S)
      END DO
      aMd(Nsh) = aMs1
      Pd(Nsh) = Ps1
      Rd(Nsh) = Rs1
      Ud(Nsh) = Us1

      aMref = aMs2
      Pref = Ps2
      Rref = Rs2
      Uref = Us2
      Sref = Ash
      DO i=Nsh+1,Nx
        S = Y(i)
        aM1 = 0.001d0
        aM2 = aMs2
        F1 = Func(aM1)
        F2 = Func(aM2)
  70    aM = 0.5d0*(aM1+aM2)
        F = Func(aM)
        IF (aM2-aM1.LE.TOL) GO TO 80
        IF (F*F1.GE.0.) THEN
          aM1 = aM
          F1 = F
        ELSE
          aM2 = aM
          F2 = F
        END IF
        GO TO 70
  80    CONTINUE
        aMd(i) = aM
        Pd(i) = Pref*((1.d0+0.5d0*Gm1*aMref*aMref)/
     &         (1.d0+0.5d0*Gm1*aMd(i)*aMd(i)))**(G/Gm1)
        Rd(i) = Rref*(Pd(i)/Pref)**(1.d0/G)
        Ud(i) = Rref*Uref*Sref/(Rd(i)*S)
      END DO

      Pref = 0.125d0*Pd(0)
      Rref = Rd(0)
      Uref = Ud(0)/1.0237498d0
      DO i=0,Nx
        Pd(i) = Pd(i)/Pref
        Rd(i) = Rd(i)/Rref
        Ud(i) = Ud(i)/Uref
      END DO
      Ps2 = Ps2/Pref
      Rs2 = Rs2/Rref
      Us2 = Us2/Uref



      END PROGRAM Choked_Nozzle

