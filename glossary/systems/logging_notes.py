
"""
Comprehensive Notes on Python Logging
-----------------------------------
This file contains examples and explanations of different logging approaches,
from basic to advanced implementations, including performance considerations.

Topics:
1. Basic setup
2. Advanced configurations
3. Developer vs User logging
4. Performance considerations
5. Environment-based logging
6. Practical examples
7. Async logging
8. Best practices

"""

import logging
import time
import asyncio
import os
from logging.handlers import RotatingFileHandler, QueueHandler
from functools import wraps
from copy import deepcopy


# ===============================================
# 1. BASIC LOGGING SETUP
# ===============================================

# Simple console-only logging
def basic_logging_setup():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

# File-only logging
def file_logging_setup():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'  # 'a' for append, 'w' for overwrite
    )
    return logging.getLogger(__name__)

# Advanced logging (both console and file)
def advanced_logging_setup():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    file_handler = RotatingFileHandler(
        'app.log',
        maxBytes=1024*1024,  # 1MB
        backupCount=5
    )
    console_handler = logging.StreamHandler()

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger


# ===============================================
# 2. SEPARATE DEVELOPER AND USER LOGGING
# ===============================================

# Create separate loggers
system_logger = logging.getLogger('system')  # For developers
user_logger = logging.getLogger('user')      # For user activity

def setup_dual_logging():
    # Developer logging (detailed, technical)
    system_logger.setLevel(logging.DEBUG)
    system_handler = logging.FileHandler('system_debug.log')
    system_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    ))
    system_logger.addHandler(system_handler)

    # User activity logging (clean, readable)
    user_logger.setLevel(logging.INFO)
    user_handler = logging.FileHandler('user_activity.log')
    user_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(message)s'
    ))
    user_logger.addHandler(user_handler)


# ===============================================
# 3. PERFORMANCE CONSIDERATIONS
# ===============================================

# Timing decorator for performance measurement
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# ===============================================
# 4. ENVIRONMENT-BASED LOGGING
# ===============================================

def configure_logging(environment='development'):
    """Configure logging based on environment"""
    if environment == 'production':
        logging.basicConfig(level=logging.WARNING)  # Minimal logging
    elif environment == 'development':
        logging.basicConfig(level=logging.DEBUG)    # Verbose logging
    elif environment == 'testing':
        logging.disable(logging.CRITICAL)           # Disable all logging


# ===============================================
# 5. PRACTICAL EXAMPLE: BANK ACCOUNT
# ===============================================

# Core logic without logging
class BankAccountCore:
    """Core business logic without logging"""
    
    def __init__(self, account_holder: str, account_number: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self._balance = initial_balance

    def transfer(self, amount: float, recipient: "BankAccountCore") -> bool:
        if amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        recipient._balance += amount
        return True

# Logged version
class BankAccount(BankAccountCore):
    """Bank Account with logging capabilities"""
    
    def __init__(self, account_holder: str, account_number: str, initial_balance: float = 0.0):
        super().__init__(account_holder, account_number, initial_balance)
        self.logger = logging.getLogger(__name__)

    @timing_decorator
    def transfer(self, amount: float, recipient: "BankAccount") -> bool:
        # Conditional logging
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug(
                f"Transfer initiated: ${amount} from {self.account_number} "
                f"to {recipient.account_number}"
            )

        try:
            result = super().transfer(amount, recipient)
            
            if result:
                self.logger.info(
                    f"Transfer successful: ${amount} from {self.account_number} "
                    f"to {recipient.account_number}"
                )
            else:
                self.logger.warning(
                    f"Transfer failed: ${amount} from {self.account_number} "
                    f"to {recipient.account_number}"
                )
            
            return result
            
        except Exception as e:
            self.logger.error(f"Transfer error: {str(e)}", exc_info=True)
            raise


# ===============================================
# 6. ASYNC LOGGING EXAMPLE
# ===============================================

class AsyncBankAccount(BankAccountCore):
    """Bank Account with async logging"""
    
    def __init__(self, account_holder: str, account_number: str):
        super().__init__(account_holder, account_number)
        self.logger = logging.getLogger(__name__)
        # Setup async handler
        async_handler = QueueHandler(asyncio.Queue())
        self.logger.addHandler(async_handler)

    async def transfer(self, amount: float, recipient: "AsyncBankAccount") -> bool:
        await self.logger.debug(f"Starting transfer of {amount}")
        result = super().transfer(amount, recipient)
        if result:
            await self.logger.info(f"Transfer successful: {amount}")
        return result


# ===============================================
# 7. USAGE EXAMPLES
# ===============================================

def main():
    # Setup logging based on environment
    env = os.getenv('ENVIRONMENT', 'development')
    configure_logging(env)
    
    # Create accounts
    account1 = BankAccount("Alice", "1234567890", 1000)
    account2 = BankAccount("Bob", "0987654321", 500)
    
    # Perform operations
    account1.transfer(100, account2)
    
    # Example of different log levels
    logger = logging.getLogger(__name__)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


if __name__ == "__main__":
    main()


"""
Key Points to Remember:
----------------------
1. Logging Levels (in order of severity):
   - DEBUG: Detailed information for debugging
   - INFO: General information about program execution
   - WARNING: Indicates a potential problem
   - ERROR: A more serious problem
   - CRITICAL: A critical problem that may prevent the program from running

2. Performance Considerations:
   - Use conditional logging (isEnabledFor)
   - Consider async logging for high-performance needs
   - Disable logging during performance testing

3. Best Practices:
   - Keep logging separate from core business logic
   - Use different logging levels for different environments
   - Don't log sensitive information
   - Use rotating file handlers for log management
   - Add log files to .gitignore

4. Testing:
   - Disable logging during tests
   - Create separate test configurations
   - Use timing decorators to measure performance
"""

