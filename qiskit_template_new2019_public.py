#for more info about qiskit install from here https://qiskit.org/documentation/install.html
#this small template code for put qubit in superposition on real quantum computing device using qiskit library from ibm
#for better performance use Python virtual environments to cleanly separate Qiskit from other applications and improve your experience, use Anaconda for windows its easy to use as in installing process on qiskit

from qiskit import *
# Create a Quantum Register with 1 qubits.
q = QuantumRegister(1)
# Create a Classical Register with 1 bits.
c = ClassicalRegister(1)
# Create a Quantum Circuit
qc = QuantumCircuit(q, c)

# Add a H gate on qubit 0, putting this qubit in superposition.
qc.h(q[0])

#measure the qubit
qc.measure(q, c)

#do save for your api once , to get your api follow instructions here https://qiskit.org/documentation/install.html
IBMQ.save_account('my api key')

provider0 = IBMQ.load_account()
backends = provider0.backends()

#print Available backends
print(backends)
#results print
#[<IBMQSimulator('ibmq_qasm_simulator') from IBMQ(hub='ibm-q', group='open', project='main')>, <IBMQBackend('ibmqx2') from IBMQ(hub='ibm-q', group='open', project='main')>, <IBMQBackend('ibmq_16_melbourne') from IBMQ(hub='ibm-q', group='open', project='main')>, <IBMQBackend('ibmq_vigo') from IBMQ(hub='ibm-q', group='open', project='main')>, <IBMQBackend('ibmq_ourense') from IBMQ(hub='ibm-q', group='open', project='main')>]


#choose one of these backends available quantum devices
quantumdevice=provider0.get_backend('ibmq_16_melbourne') #this used but better to use according to how many qbit you need

job = execute(qc, quantumdevice, shots=1024)
result = job.result()
counts = result.get_counts(qc)
print("\nTotal count for 0,1 are:",counts)

#Total count for 00 and 11 are: {'0': 526, '1': 474}
#{'0': 543, '1': 481}
